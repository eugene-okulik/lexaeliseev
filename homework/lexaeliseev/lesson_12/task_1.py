class Flower:
    """Общий класс для всех цветов"""

    def __init__(self, name, color: str, length: int, price: int, life: int):
        self.name = name
        self.color = color
        self.length = length
        self.price = price
        self.life = life

    def __str__(self):
        return f"{self.name} ({self.color}), " \
               f"длина: {self.length} см., " \
               f"цена: {self.price} руб, " \
               f"время жизни(дней): {self.life}"


class Rose(Flower):
    """Класс для Розы"""
    def __init__(self, color, length, price, life=7):
        super().__init__("Роза", color, length, price, life)


class Chamomile(Flower):
    """Класс для Ромашки"""
    def __init__(self, color, length, price, life=3):
        super().__init__("Ромашка", color, length, price, life)


class Peony(Flower):
    """Класс для Пиона"""
    def __init__(self, color, length, price, life=2):
        super().__init__("Пион", color, length, price, life)


class Bouquet:
    """Класс Букет"""

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        """Добавление цветка в букет"""
        self.flowers.append(flower)

    def __str__(self):
        bouquet = "Мой букет:\n"
        for flower in self.flowers:
            bouquet = f"{bouquet} + {str(flower)} + \n"
        return bouquet

    def total_price(self):
        """Метод определения стоимости букета"""
        total = 0
        for flower in self.flowers:
            total = total + flower.price
        return total

    def flowers_time(self):
        """Метод определения продолжительности средней жизни букета"""
        if not self.flowers:
            return 0
        total_life = 0
        for flower in self.flowers:
            total_life = total_life + flower.life
        return int(total_life / len(self.flowers))

    def _get_life(self, flower):
        """Получение среднего времени жизни"""
        return flower.life

    def sort_by_life(self, reverse=False):
        """Сортировка по времени свежести"""
        return sorted(self.flowers, key=self._get_life, reverse=reverse)

    def _get_price(self, flower):
        """Получение цены"""
        return flower.price

    def sort_by_price(self, reverse=False):
        """Сортировка по стоимости"""
        return sorted(self.flowers, key=self._get_price, reverse=reverse)

    def find_name(self, name):
        """Поиск цветов по названию"""
        result = []
        for flower in self.flowers:
            if flower.name == name:
                result.append(flower)
        if not result:
            print("По вашему запросу ничего не найдено")
        return result


""" Создать экземпляры (объекты) цветов разных видов. """
rose = Rose("Бордовый", 60, 250, 6)
chamomile = Chamomile("Белый", 40, 110, 9)
peony = Peony("Лиловый", 50, 300, 4)
rose2 = Rose("Красный", 55, 200, 5)

""" Собрать букет """
my_bouquet = Bouquet()
my_bouquet.add_flower(rose)
my_bouquet.add_flower(chamomile)
my_bouquet.add_flower(peony)
my_bouquet.add_flower(rose2)

""" Печать букета """
print(my_bouquet)

""" Определение стоимости букета """
print(f"Стоимость букета: {my_bouquet.total_price()} руб.")

""" Определение средней продолжительности жизни букета """
print(f"Среднее время свежести: {my_bouquet.flowers_time()} дней")

""" Cортировка """
print()
for flower in my_bouquet.sort_by_price():
    print(f"Сортировка от меньшей цены к большей {flower}")

print()
for flower in my_bouquet.sort_by_price(True):
    print(f"Сортировка от большей цены к меньшей {flower}")

""" Поиск """
print()
for flower in my_bouquet.find_name("Пум пум}"):
    print(f"Результаты вашего поиска: {flower}")

for flower in my_bouquet.find_name("Пион"):
    print(f"Результаты вашего поиска: {flower}")
