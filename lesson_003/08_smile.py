# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

sd.resolution = (1200, 600)


def smile_draw(point, color):
    smile_width = 1
    # Ellipse:
    left_bottom = sd.get_point(point.x - 50, point.y - 50)
    right_top = sd.get_point(point.x + 50, point.y + 50)
    sd.ellipse(left_bottom=left_bottom, right_top=right_top, color=color, width=smile_width)
    # Eyes:
    eye_radius = 10
    left_eye_center = sd.get_point(point.x - 20, point.y + 20)
    right_eye_center = sd.get_point(point.x + 20, point.y + 20)
    sd.circle(center_position=left_eye_center, radius=eye_radius, color=color, width=smile_width)
    sd.circle(center_position=right_eye_center, radius=eye_radius, color=color, width=smile_width)
    # Mouth
    first_point = sd.get_point(point.x - 30, point.y - 5)
    second_point = sd.get_point(point.x - 15, point.y - 15)
    third_point = sd.get_point(point.x + 15, point.y - 15)
    fourth_point = sd.get_point(point.x + 30, point.y - 5)
    mouth_points = [first_point, second_point, third_point, fourth_point]
    sd.lines(point_list=mouth_points, color=color, closed=False, width=smile_width)
    return 'Work complete!'


for i in range(1, 11):
    smile_draw(sd.random_point(), sd.random_color())

sd.pause()
