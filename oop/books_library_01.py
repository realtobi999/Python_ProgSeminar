import os
import iridis


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if not self.available:
            raise ValueError(f"Kniha '{self.title} je již vypůjčená.'")
        self.available = False

    def return_book(self):
        if self.available:
            raise ValueError(f"Kniha '{self.title} již byla dostupná.'")
        self.available = True

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year}) | Stav: {"Dostupná" if self.available else "Nedostupná"}"


# Seznam knih v knihovně
library = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("Mistr a Markétka", "Michail Bulgakov", 1967),
    Book("Malý princ", "Antoine de Saint-Exupéry", 1943),
]

os.system("clear" if os.name == "posix" else "cls")

# Výpis knih v knihovně
iridis.print_with_color("--- Seznam knih v knihovně: ---\n", color=iridis.Color.BOLD_GREEN)
for book in library:
    print(str(book))

# Simulace vypůjčení a vrácení knihy
iridis.print_with_color("\n--- Test vypůjčení a vrácení knih ---\n", color=iridis.Color.BOLD_GREEN)

library[0].borrow()
try:
    library[0].borrow()  # Pokus o vypůjčení již vypůjčené knihy
except ValueError as e:
    print(e)

library[0].return_book()
try:
    library[0].return_book()  # Pokus o vrácení již dostupné knihy
except ValueError as e:
    print(e)

# Znovu vypíšeme knihovnu po změnách
iridis.print_with_color("\n--- Aktualizovaný seznam knih v knihovně: ---\n", color=iridis.Color.BOLD_GREEN)
for book in library:
    print(str(book))

input("\n")
