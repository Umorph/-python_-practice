# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger


def bread_adding():
    print('Возьмем булочки')

    recipe_component = ('Булочка', 1)
    return recipe_component


def patty_adding():
    print('А теперь добавим котлету')

    recipe_component = ('Котлета', 1)
    return recipe_component


def cucumber_adding():
    print('А теперь добавим 4 огурчика')

    recipe_component = ('Огурчики', 4)
    return recipe_component


def tomato_adding():
    print('А теперь добавим 2 помидора')

    recipe_component = ('Помидорки', 2)
    return recipe_component


def mayo_adding():
    print('Теперь добавим майонез')

    recipe_component = ('Майонез', 1)
    return recipe_component


def cheese_adding():
    print('Теперь добавим сыр')

    recipe_component = ('Сыр', 1)
    return recipe_component


def double_cheeseburger_recipe(count):
    recipe = {}
    for _ in range(0, count):
        ingredient = bread_adding()
        recipe[ingredient[0]] = ingredient[1]

        ingredient = patty_adding()
        recipe[ingredient[0]] = ingredient[1]

        ingredient = cheese_adding()
        recipe[ingredient[0]] = ingredient[1]

        ingredient = patty_adding()
        recipe[ingredient[0]] = ingredient[1]

        ingredient = cheese_adding()
        recipe[ingredient[0]] = ingredient[1]

        ingredient = cucumber_adding()
        recipe[ingredient[0]] = ingredient[1]

        ingredient = mayo_adding()
        recipe[ingredient[0]] = ingredient[1]

        ingredient = tomato_adding()
        recipe[ingredient[0]] = ingredient[1]

        ingredient = bread_adding()
        recipe[ingredient[0]] = ingredient[1]

        return recipe


print(double_cheeseburger_recipe(1))