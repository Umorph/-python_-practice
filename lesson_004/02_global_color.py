# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1600, 900)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def shape_draw(point, angle, side_length):
    shapes_parameters_dict = {
        'triangle': {'vertices': 3, 'angle': 120},
        'square': {'vertices': 4, 'angle': 90},
        'pentagon': {'vertices': 5, 'angle': 72},
        'hexagon': {'vertices': 6, 'angle': 60}
    }
    shape_codes_dict = {
        '0': 'triangle',
        '1': 'square',
        '2': 'pentagon',
        '3': 'hexagon'
    }
    shape_colors_dict = {
        '0': 'COLOR_RED',
        '1': 'COLOR_ORANGE',
        '2': 'COLOR_YELLOW',
        '3': 'COLOR_GREEN',
        '4': 'COLOR_CYAN',
        '5': 'COLOR_BLUE',
        '6': 'COLOR_PURPLE'
    }
    color_parameters_dict = {
        'COLOR_RED': (255, 0, 0),
        'COLOR_ORANGE': (255, 127, 0),
        'COLOR_YELLOW': (255, 255, 0),
        'COLOR_GREEN': (0, 255, 0),
        'COLOR_CYAN': (0, 255, 255),
        'COLOR_BLUE': (0, 0, 255),
        'COLOR_PURPLE': (255, 0, 255)
    }

    start_point = point

    for shape in shape_codes_dict:
        print(shape, ' - ', shape_codes_dict[shape])
    user_input = input('Choose the shape: ')
    if user_input.isnumeric:
        user_input = int(user_input)
        if 0 <= user_input <= 3:
            user_input = str(user_input)
            shape_name = shape_codes_dict.get(user_input)
            shape_parameters = shapes_parameters_dict.get(shape_name)
            vertices_count = shape_parameters.get('vertices')
            angle_increment = shape_parameters.get('angle')

            for color in shape_colors_dict:
                print(color, ' - ', shape_colors_dict[color])
            user_color = input('Choose the color: ')
            if user_color.isnumeric():
                user_color = int(user_color)
                if 0 <= user_color <= 6:
                    user_color = str(user_color)
                    shape_color_name = shape_colors_dict.get(user_color)
                    shape_color_code = color_parameters_dict.get(shape_color_name)
                else:
                    print('Wrong color code, enter the number between 0 and 6')
                    return None
            else:
                print('Wrong color code, enter the number, not text')
                return None

            for _ in range(1, vertices_count):
                current_vector = sd.get_vector(start_point=point, angle=angle, length=side_length, width=1)
                current_vector.draw(color=shape_color_code)
                angle += angle_increment
                point = current_vector.end_point
            sd.line(start_point=start_point, end_point=point, color=shape_color_code, width=1)
        else:
            print('Wrong shape code, enter the number between 0 and 3')
    else:
        print('Wrong shape code, enter the number, not text')


for y in range(100, 601, 500):
    for x in range(100, 601, 500):
        current_point = sd.get_point(x, y)
        shape_draw(point=current_point, angle=0, side_length=100)

sd.pause()
