

def __lt__():   # less than

    pass


def __gt__():    # greter than

    pass


def __le__():    # less or equle

    pass


def __ge__():    # greter or equle

    pass


def __add__():  # сложение

    pass



def __lt__(self, obj):   # less than

    return self.avg_temp < obj.avg_temp


def __le__(self, obj):   # less than

    return self.avg_temp <= obj.avg_temp


# print(data1 < data2) # это объекты класса


def __add__(self, obj):  # сложение

    return [self, obj]