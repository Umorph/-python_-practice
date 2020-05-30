# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1680, 920)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(500, 200)
radius = 50
for _ in range(3):
    sd.circle(point, radius, color=[10, 150, 10])
    radius += 5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=[150, 10, 10], width=2)


point = sd.get_point(300, 300)
bubble(point=point, step=10)

# Нарисовать 10 пузырьков в ряд
y = 500
x = 100
while x < 1001:
    point = sd.get_point(x, y)
    radius = 50
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, color=[150, 120, 50], width=2)
        radius += 5
    x += 100

# Нарисовать три ряда по 10 пузырьков
y = 100
for _ in range(3):
    x = 100
    while x < 1001:
        point = sd.get_point(x, y)
        radius = 25
        for _ in range(3):
            sd.circle(center_position=point, radius=radius, color=[180, 10, 100], width=1)
            radius += 5
        x += 100
    y += 100


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    bubble(point=point, step=5)

sd.pause()
