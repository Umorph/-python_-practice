# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1600, 900)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle_draw(point, angle, length):
    for _ in range(1, 4):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        vector.draw()
        angle += 120
        point = vector.end_point


def square_draw(point, angle, length):
    for _ in range(1, 5):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        vector.draw()
        angle += 90
        point = vector.end_point


def pentagon_draw(point, angle, length):
    for _ in range(1, 6):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        vector.draw()
        angle += 72
        point = vector.end_point


def hexagon_draw(point, angle, length):
    for _ in range(1, 7):
        vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        vector.draw()
        angle += 60
        point = vector.end_point


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)


def shape_draw(point, angle, side_length, shape):
    shapes_parameters = {
        'triangle': {'vertices': 3, 'angle': 120},
        'square': {'vertices': 4, 'angle': 90},
        'pentagon': {'vertices': 5, 'angle': 72},
        'hexagon': {'vertices': 6, 'angle': 60}
    }

    current_shape = shapes_parameters.get(shape)
    vertices_count = current_shape.get('vertices')
    angle_increment = current_shape.get('angle')

    for _ in range(0, vertices_count):
        current_vector = sd.get_vector(start_point=point, angle=angle, length=side_length, width=1)
        current_vector.draw()
        angle += angle_increment
        point = current_vector.end_point


triangle_point = sd.get_point(200, 100)
square_point = sd.get_point(200, 300)
pentagon_point = sd.get_point(200, 500)
hexagon_point = sd.get_point(200, 700)

shape_draw(triangle_point, 0, 100, 'triangle')
shape_draw(square_point, 0, 100, 'square')
shape_draw(pentagon_point, 0, 100, 'pentagon')
shape_draw(hexagon_point, 0, 100, 'hexagon')


# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
