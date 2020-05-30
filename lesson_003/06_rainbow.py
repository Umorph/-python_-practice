# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1620, 940)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x1 = 50
x2 = 350
for current_color in rainbow_colors:
    point_1 = sd.get_point(x1, 50)
    point_2 = sd.get_point(x2, 450)
    sd.line(point_1, point_2, current_color, 4)
    x1 += 5
    x2 += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
radius = 800
for current_color in rainbow_colors:
    center = sd.get_point(1620, 0)
    sd.circle(center, radius, current_color, 50)
    radius += 50

sd.pause()
