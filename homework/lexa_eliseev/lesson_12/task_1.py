"""
    Создать классы цветов: общий класс для всех цветов и классы для нескольких видов. 
    Создать экземпляры (объекты) цветов разных видов. 
    Собрать букет (букет - еще один класс) с определением его стоимости. В букете цветы пусть хранятся в списке. 
    Это будет список объектов.
    Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.

    Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
    Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).
"""


class Flower:
    """ Создать классы цветов: общий класс для всех цветов"""

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
    """Собрать букет (букет - еще один класс)"""
    def __init__(self):
        self.flowers = []

    # def __add__(self, obj):  # сложение подумать, не получилось
    #     return [self, obj]

    def add_flower(self, flower):
        """Метод создания букета"""
        self.flowers.append(flower)

    def __str__(self):
        bouquet = f"Мой букет:\n"
        for flower in self.flowers:
            bouquet = bouquet + str(flower) + "\n"
        return bouquet

    def life(self):
        """Метод определения продолжительности средней жизни букета"""
        count = []
        for flower in self.flowers:
            count.append(flower.life)
        total = sum(count)
        return total / len(count)

    def total_sum(self):
        """Метод определения стоимости букета"""
        total = []
        for flower in self.flowers:
            total.append(flower.price)
        total = int(sum(total))
        return total

    def sorti(self):
        result = sorted(self.flowers)
        return result

    def get_life(self, flower):
        return flower.life

    def sorted_1(self):
        return sorted(self.flowers, key=self.get_life)


""" Создать экземпляры (объекты) цветов разных видов. """
rose = Rose("Бордовый", 60, 250, 6)
chamomile = Chamomile("Белый", 40, 110, 9)
peony = Peony("Лиловый", 50, 300, 4)

"""Собрать букет"""
my_bouquet = Bouquet()
my_bouquet.add_flower(rose)
my_bouquet.add_flower(chamomile)
my_bouquet.add_flower(peony)
print(my_bouquet)

"""Определение стоимости букета"""
print(my_bouquet.total_sum())

"""Определение средней продолжительности жизни букета"""
print(my_bouquet.life())


print(my_bouquet.flowers[1].name)
for i in my_bouquet.flowers:
    print(i.name)


print(my_bouquet.sorted_1)

for f in my_bouquet.sorted_1():
    print(f)