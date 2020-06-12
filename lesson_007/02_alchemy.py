# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __init__(self):
        self.name = 'Вода'
        self.type = 'water'

    def __add__(self, other):
        if other.type == 'air':
            return Storm().name
        elif other.type == 'fire':
            return Steam().name
        elif other.type == 'earth':
            return Dirt().name
        else:
            return 'Такого элемента нет'

    def __str__(self):
        return self.name


class Air:
    def __init__(self):
        self.name = 'Воздух'
        self.type = 'air'

    def __add__(self, other):
        if other.type == 'water':
            return Storm().name
        elif other.type == 'fire':
            return Lightning().name
        elif other.type == 'earth':
            return Dust().name
        elif other.type == 'steam':
            return Cloud().name
        else:
            return 'Такого элемента нет'

    def __str__(self):
        return self.name


class Fire:
    def __init__(self):
        self.name = 'Огонь'
        self.type = 'fire'

    def __add__(self, other):
        if other.type == 'water':
            return Steam().name
        elif other.type == 'air':
            return Lightning().name
        elif other.type == 'earth':
            return Lava().name
        else:
            return 'Такого элемента нет'

    def __str__(self):
        return self.name


class Earth:
    def __init__(self):
        self.name = 'Земля'
        self.type = 'earth'

    def __add__(self, other):
        if other.type == 'water':
            return Dirt().name
        elif other.type == 'air':
            return Dust().name
        elif other.type == 'fire':
            return Lava().name
        else:
            return 'Такого элемента нет'

    def __str__(self):
        return self.name


class Storm:
    def __init__(self):
        self.name = 'Шторм'
        self.type = 'storm'

    def __add__(self, other):
        return 'Такой комбинации нет'

    def __str__(self):
        return self.name


class Steam:
    def __init__(self):
        self.name = 'Пар'
        self.type = 'steam'

    def __add__(self, other):
        if other.type == 'air':
            return Cloud().name
        else:
            return 'Такой комбинации нет'

    def __str__(self):
        return self.name


class Dirt:
    def __init__(self):
        self.name = 'Грязь'
        self.type = 'dirt'

    def __add__(self, other):
        return 'Такого элемента нет'

    def __str__(self):
        return self.name


class Lightning:
    def __init__(self):
        self.name = 'Молния'
        self.type = 'lightning'

    def __add__(self, other):
        return 'Такой комбинации нет'

    def __str__(self):
        return self.name


class Dust:
    def __init__(self):
        self.name = 'Пыль'
        self.type = 'dust'

    def __add__(self, other):
        return 'Такой комбинации нет'

    def __str__(self):
        return self.name


class Lava:
    def __init__(self):
        self.name = 'Лава'
        self.type = 'lava'

    def __add__(self, other):
        return 'Такой комбинации нет'

    def __str__(self):
        return self.name


class Cloud:
    def __init__(self):
        self.name = 'Облако'
        self.type = 'cloud'

    def __add__(self, other):
        return 'Такой кобминации нет'

    def __str__(self):
        return self.name


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Air(), '+', Steam(), '=', Air() + Steam())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
