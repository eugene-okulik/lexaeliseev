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


class SchoolBook(Book):
    def __init__(self, title_book: str, author_book: str, count_pages: int, isbn: str,
                 subject: str, group: int, example=True, reservation=False):
        super().__init__(title_book, author_book, count_pages, isbn, reservation)
        self.subject = subject
        self.group = group
        self.example = example


book_1 = Book("Идиот", "Достоевский", 500, "2-266-11156-6", reservation=False)
book_2 = Book("Дарт Бэйн: Путь разрушения", "Дрю Карпишин", 416, "1003—1000 ДБЯ", reservation=False)
book_3 = Book("Дарт Бэйн: Правило двух", "Дрю Карпишин", 352, "1000 — 990 ДБЯ", reservation=False)
book_4 = Book("Дарт Бэйн: Династия зла", "Дрю Карпишин", 352, "980 ДБЯ", reservation=False)
book_5 = Book("Дарт Плэгас»", "Джеймс Лучено", 428, "67 ДБЯ — 65 ДБЯ", reservation=True)

print(f"Название: {book_1.title_book}, "
      f"Автор: {book_1.author_book}, "
      f"страниц: {book_1.count_pages}, "
      f"материал: {book_1.page_material}"
      f"{book_1.reservation_status()}")

print(f"Название: {book_2.title_book}, "
      f"Автор: {book_2.author_book}, "
      f"страниц: {book_2.count_pages}, "
      f"материал: {book_2.page_material}"
      f"{book_2.reservation_status()}")

print(f"Название: {book_3.title_book}, "
      f"Автор: {book_3.author_book}, "
      f"страниц: {book_3.count_pages}, "
      f"материал: {book_3.page_material}"
      f"{book_3.reservation_status()}")

print(f"Название: {book_4.title_book}, "
      f"Автор: {book_4.author_book}, "
      f"страниц: {book_4.count_pages}, "
      f"материал: {book_4.page_material}"
      f"{book_4.reservation_status()}")

print(f"Название: {book_5.title_book}, "
      f"Автор: {book_5.author_book}, "
      f"страниц: {book_5.count_pages}, "
      f"материал: {book_5.page_material}"
      f"{book_5.reservation_status()}")

book_6 = SchoolBook("Алгебра", "Иванов И.С.", 321, "2-266-11456-4", "Математика", 7)
book_7 = SchoolBook("Литература для продвинутых", "Петров П.А.", 643, "2-266-5356-1", "Литература", 10, example=False)
book_8 = SchoolBook("Химия", "Самсонова А.А.", 323, "2-166-356-7", "Химия", 9, reservation=True)

print(f"Название: {book_6.title_book}, "
      f"Автор: {book_6.author_book}, "
      f"страниц: {book_6.count_pages}, "
      f"предмет: {book_6.subject}, "
      f"класс: {book_6.group}"
      f"{book_6.reservation_status()}")

print(f"Название: {book_7.title_book}, "
      f"Автор: {book_7.author_book}, "
      f"страниц: {book_7.count_pages}, "
      f"предмет: {book_7.subject}, "
      f"класс: {book_7.group}"
      f"{book_7.reservation_status()}")

print(f"Название: {book_8.title_book}, "
      f"Автор: {book_8.author_book}, "
      f"страниц: {book_8.count_pages}, "
      f"предмет: {book_8.subject}, "
      f"класс: {book_8.group}"
      f"{book_8.reservation_status()}")
