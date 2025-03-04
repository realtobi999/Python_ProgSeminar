import datetime
import json
import os
import iridis


class Book:
    def __init__(self, title: str, author: str, year: int, available: bool = True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def borrow(self):
        if not self.available:
            raise ValueError(f"Kniha '{self.title}' je již vypůjčená.")
        self.available = False

    def return_book(self):
        if self.available:
            raise ValueError(f"Kniha '{self.title}' již byla dostupná.")
        self.available = True

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year}) | Stav: {'Dostupná' if self.available else 'Nedostupná'}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.available,
        }

    # Static methods.

    @staticmethod
    def is_valid_year(year):
        return 1440 <= year <= datetime.datetime.now().year

    @staticmethod
    def parse_from_string(str_book: str):
        parts = str_book.split(";")
        if len(parts) != 3:
            raise ValueError("Neplatný řetězec pro inicializaci knihy.")

        return Book(title=parts[0], author=parts[1], year=int(parts[2]))


class Ebook(Book):
    def __init__(self, title, author, year, file_format):
        super().__init__(title, author, year)
        self.file_format = file_format

    def __str__(self):
        return super().__str__() + f" | Formát: {self.file_format}"


class AudioBook(Book):
    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    def __str__(self):
        return super().__str__() + f" | Délka: {self.duration}"


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def remove_book(self, book: Book):
        self.__books.remove(book)

    def list_books(self):
        for i, book in enumerate(self.__books):
            print(f"{i}. {str(book)}")

    def save_in_json(self, file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self.__books], f, ensure_ascii=False, indent=4)

    # Static Methods.

    @staticmethod
    def parse_from_json(file_path):
        library = Library()
        with open(file_path, "r", encoding="utf-8") as f:
            for book in json.load(f):
                library.add_book(
                    Book(book["title"], book["author"], book["year"], book["available"])
                )
        return library

JSON_FILE_PATH = "./data/books.json"

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")

    # Načtení knih z JSON souboru.
    library = Library.parse_from_json(JSON_FILE_PATH)

    # Výpis knih v knihovně.
    iridis.print_with_color("--- Seznam knih v knihovně: ---\n", color=iridis.Color.BOLD_GREEN)
    library.list_books()

    library.save_in_json(JSON_FILE_PATH)
