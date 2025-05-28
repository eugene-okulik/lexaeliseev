class Book:
    page_material = "бумага"
    presence_of_text = True

    def __init__(self, title_book: str, author_book: str, count_pages: int, isbn: str, reservation=False):
        self.title_book = title_book
        self.author_book = author_book
        self.count_pages = count_pages
        self.isbn = isbn
        self.reservation = reservation

    def reservation_status(self):
        return ", зарезервирована" if self.reservation is True else ""

    def __str__(self):
        return (
            f"Название: {self.title_book}, "
            f"Автор: {self.author_book}, "
            f"страниц: {self.count_pages}, "
            f"предмет: {self.page_material} "
            f"{self.reservation_status()}"
        )


class SchoolBook(Book):
    def __init__(self, title_book: str, author_book: str, count_pages: int, isbn: str,
                 subject: str, group: int, example=True, reservation=False):
        super().__init__(title_book, author_book, count_pages, isbn, reservation)
        self.subject = subject
        self.group = group
        self.example = example

    def __str__(self):
        return (
            f"Название: {self.title_book}, "
            f"Автор: {self.author_book}, "
            f"страниц: {self.count_pages}, "
            f"предмет: {self.page_material} "
            f"{self.reservation_status()}")

book_1 = Book("Идиот", "Достоевский", 500, "2-266-11156-6", reservation=False)
book_2 = Book("Дарт Бэйн: Путь разрушения", "Дрю Карпишин", 416, "1003—1000 ДБЯ", reservation=False)
book_3 = Book("Дарт Бэйн: Правило двух", "Дрю Карпишин", 352, "1000 — 990 ДБЯ", reservation=False)
book_4 = Book("Дарт Бэйн: Династия зла", "Дрю Карпишин", 352, "980 ДБЯ", reservation=False)
book_5 = Book("Дарт Плэгас»", "Джеймс Лучено", 428, "67 ДБЯ — 65 ДБЯ", reservation=True)

print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)

book_6 = SchoolBook("Алгебра", "Иванов И.С.", 321, "2-266-11456-4", "Математика", 7)
book_7 = SchoolBook("Литература для продвинутых", "Петров П.А.", 643, "2-266-5356-1", "Литература", 10, example=False)
book_8 = SchoolBook("Химия", "Самсонова А.А.", 323, "2-166-356-7", "Химия", 9, reservation=True)

print(book_6)
print(book_7)
print(book_8)
