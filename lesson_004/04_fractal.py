# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

sd.resolution = (1600, 900)


def draw_bunches(start_point, angle, length):
    if length >= 10:
        first_vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        first_vector.draw()
        start_point = first_vector.end_point
        draw_bunches(start_point=start_point, angle=angle + 30, length=length * 0.85)
        draw_bunches(start_point=start_point, angle=angle - 30, length=length * 0.85)
    else:
        return


# root_point = sd.get_point(800, 30)
# draw_bunches(start_point=root_point, angle=90, length=200)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_bunches_random(start_point, angle, length):
    if length >= 20:
        first_vector = sd.get_vector(start_point=start_point, angle=angle, length=length)
        first_vector.draw()
        start_point = first_vector.end_point
        length_coeff_1 = sd.random_number(90, 95)
        length_coeff_1 = length_coeff_1 / 100
        length_coeff_2 = sd.random_number(90, 95)
        length_coeff_2 = length_coeff_2 / 100
        draw_bunches_random(start_point=start_point,
                     angle=angle + sd.random_number(15,35),
                     length=length * length_coeff_1)
        draw_bunches_random(start_point=start_point,
                     angle=angle - sd.random_number(15, 40),
                     length=length * length_coeff_2)
    else:
        return


root_point = sd.get_point(800, 30)
draw_bunches_random(start_point=root_point, angle=90, length=70)

sd.pause()
