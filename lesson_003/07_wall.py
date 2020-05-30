# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

simple_draw.resolution = (1600, 800)

y1 = 0
left_shift = False

for y1 in range(0, 800, 50):
    x1 = 0
    if left_shift:
        range_start = -50
        range_end = 1500
        left_shift = False
    else:
        range_start = 0
        range_end = 1600
        left_shift = True
    for x1 in range(range_start, range_end, 100):
        # Расчитываем координаты точек
        x2 = x1 + 100
        y2 = y1 + 50
        # Расчитываем точки
        point_1 = simple_draw.get_point(x1, y1)
        point_2 = simple_draw.get_point(x2, y2)
        # Строим прямоугольник по точкам
        simple_draw.rectangle(point_1, point_2, (150, 10, 10), 1)

simple_draw.pause()
