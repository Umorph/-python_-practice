# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class House:
    def __init__(self):
        self.bowl = 20
        self.mess = 0
        self.human_food = 100
        self.cat_food = 80
        self.money = 200

    def __str__(self):
        return 'Дома: {} - еды в мисках, {} грязи, {} человеческой еды, {} кошачей еды, ' \
               'денег - {}'.format(self.bowl,
                                   self.mess,
                                   self.human_food,
                                   self.cat_food,
                                   self.money)


class Cat:
    def __init__(self):
        self.house = None
        self.name = 'Барсик'
        self.fullness = 50
        self.energy = 150
        self.mood = 100

    def eat(self):
        if self.house.bowl > 0:
            print('{} поела немного Вискаса'.format(self.name))
            self.house.bowl -= 10
            self.fullness += 50
            self.energy -= 15
            self.mood += 20
        else:
            print('{} хотела поесть, но в миске пусто'.format(self.name))
            self.fullness -= 10
            self.mood -= 20
            self.energy -= 30

    def sleep(self):
        print('{} отрубилась спать!'.format(self.name))
        self.fullness -= 15
        self.energy += 150
        self.mood += 10

    def tear_wallpaper(self):
        print('{} дерет обои и ей поебать'.format(self.name))
        self.fullness -= 30
        self.energy -= 50
        self.mood += 100
        self.house.mess += 10

    def poop(self):
        if self.house.mess <= 50:
            print('{} покакала от души'.format(self.name))
            self.mood += 30
        else:
            print('{} понимает, что лоток весь в говне и превозмогает'.format(self.name))
            self.mood -= 50

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness < 0:
            print('{} умерла от голода'.format(self.name))
            return
        else:
            if self.fullness < 30:
                self.eat()
                return
            elif self.energy < 30:
                self.sleep()
                return
            elif self.mood < 30:
                self.tear_wallpaper()
                return
            else:
                dice = randint(1, 6)
                if dice == 1 or dice == 4:
                    self.poop()
                    return
                if dice == 2:
                    print('{} чекинится на подоконнике'.format(self.name))
                    self.fullness -= 10
                    self.energy += 50
                    self.mood += 20
                    return
                else:
                    print('{} пидарасится по всей квартире'.format(self.name))
                    self.fullness -= 40
                    self.energy -= 50
                    self.mood += 50
                    return

    def __str__(self):
        return '{}, сытость - {}, энергия - {}, настроение - {}'.format(self.name, self.fullness,
                                                                        self.energy, self.mood)


class Human:
    def __init__(self):
        self.house = None
        self.name = 'Вася'
        self.fullness = 10

    def feed(self):
        print('{} Кладет пакетик корма в миски'.format(self.name))
        self.house.cat_food -= 20
        self.house.bowl += 20

    def eat(self):
        if self.house.human_food >= 20:
            print('{} ест дошик'.format(self.name))
            self.fullness += 50
            self.house.human_food -= 20
        else:
            print('{} осознает, что жрать нечего')

    def clean(self):
        print('{} убирается в квартире'.format(self.name))
        self.house.mess = 0
        self.fullness -= 25

    def work(self):
        print('{} пиздохает на работу'.format(self.name))
        self.fullness -= 25
        self.house.money += 200

    def shopping(self):
        print('{} идет в магазин за продуктами'.format(self.name))
        self.house.cat_food += 100
        self.house.human_food += 200
        self.house.money -= 100
        self.fullness -= 25

    def play_dota(self):
        print('{} Играет в доту'.format(self.name))
        self.fullness -= 25

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness < 0:
            print('{} погибает от голода'.format(self.name))
            return
        else:
            if self.fullness <= 25:
                self.eat()
                return
            elif House().bowl == 0:
                self.feed()
                return
            elif House().human_food == 0 or House().cat_food == 0:
                self.shopping()
                return
            elif House().money <= 100:
                self.work()
                return
            else:
                dice = randint(1, 7)
                if dice == 1:
                    self.work()
                    return
                if dice > 5:
                    self.eat()
                    return
                else:
                    self.play_dota()
                    return

    def __str__(self):
        return '{}, сытость - {}'.format(self.name, self.fullness)


eva = Cat()
eva.name = 'Ева'

motorola = Cat()
motorola.name = 'Мотя'

overlord = Human()
overlord.name = 'Валдес'

sunshine = Human()
sunshine.name = 'Солнце'

base = House()

eva.go_to_the_house(house=base)
motorola.go_to_the_house(house=base)
overlord.go_to_the_house(house=base)
sunshine.go_to_the_house(house=base)


for day in range(1, 6):
    cprint('============================== День {} =============================='.format(day), color='yellow')
    for time in range(0, 15, 5):
        current_time = str(time + 8) + ':00'
        cprint('===== {} ====='.format(current_time), color='blue')
        overlord.act()
        eva.act()
        motorola.act()
        sunshine.act()
        cprint('----- Статус -----', color='red')
        print(overlord)
        print(eva)
        print(motorola)
        print(sunshine)
        print(House())
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
