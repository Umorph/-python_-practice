# -*- coding: utf-8 -*-

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок (N = 20)
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

import simple_draw as sd
from random import randint

sd.resolution = (1200, 900)
sd.caption = 'Snowflake v2.34'

coordinates_list = []


def generate_points():
    y = 900
    for _ in range(0, 1):
        x = randint(0, 1200)
        length = randint(30, 50)
        snowflake_coordinates = dict(x=x, y=y, length=length)
        coordinates_list.append(snowflake_coordinates)
    return coordinates_list


def draw_snowflakes(points_list):
    for coordinates in points_list:
        x = coordinates['x']
        y = coordinates['y']
        length = coordinates['length']
        if y > 0:
            center = sd.get_point(x=x, y=y)
            sd.snowflake(center=center, length=length)
        else:
            points_list.remove(coordinates)
    return True


def snowflake_animates(points_list):
    for coordinates in points_list:
        coordinates['x'] += randint(-50, 50)
        coordinates['y'] -= randint(30, 60)


while True:
    sd.clear_screen()
    points = generate_points()
    draw_snowflakes(points_list=points)
    snowflake_animates(points_list=points)
    sd.sleep(0.1)

