class Book:
    material = 'бумага'
    is_text = True
    isbn = "isbn"

    def __init__(self, title_book, autor, count_pages, reservation=False):
        self.title_book = title_book
        self.autor = autor
        self.count_pages = count_pages
        self.reservation_status = reservation

    def reservation(self):
        if self.reservation_status is True:
            return ', зарезервирована'
        elif self.reservation_status is False:
            return ''

    def print_info(self):
        print(f"Название: {self.title_book},"
              f" Автор: {self.autor},"
              f" страниц: {self.count_pages},"
              f" материал: {self.material}"
              f"{self.reservation()}")


book_1 = Book('Идиот', 'Достоевский', 500, False)
book_2 = Book('Мастер и Маргарита', 'Булгаков', 650, False)
book_3 = Book('Преступление и наказание', 'Достоевский', 450, False)
book_4 = Book('Евгений Онегин', 'Пушкин', 250, False)
book_5 = Book('Тихий Дон', 'Шолохов', 900, True)


book_1.print_info()
book_2.print_info()
book_3.print_info()
book_4.print_info()
book_5.print_info()


class SchoolBook(Book):

    def __init__(self, title_book, autor, count_pages, subject, group, reservation=False, is_example=True):
        super().__init__(title_book, autor, count_pages, reservation)

        self.subject = subject
        self.group = group
        self.is_example = is_example

    def print_info(self):
        print(f"Название: {self.title_book}, "
              f"Автор: {self.autor}, "
              f"страниц: {self.count_pages}, "
              f"предмет: {self.subject}, "
              f"класс: {self.group}"
              f"{self.reservation()}")


book_6 = SchoolBook("Алгебра", "Иванов", 200, "Математика", 9)
book_7 = SchoolBook("Физика", "Петров", 350, "Естественные науки", 10)
book_8 = SchoolBook("История России", "Сидоров", 280, "Гуманитарные науки", 8)
book_9 = SchoolBook("Химия", "Кузнецова", 320, "Естественные науки", 11)
book_10 = SchoolBook("Литература", "Смирнова", 400, "Гуманитарные науки", 7, reservation=True)

book_6.print_info()
book_7.print_info()
book_8.print_info()
book_9.print_info()
book_10.print_info()
