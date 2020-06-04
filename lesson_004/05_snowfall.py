# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 700)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок (N = 20)
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

snowflake_coordinates = [
    (100, 50),
    (50, 100)
]

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

while True:
    sd.clear_screen()
    for coordinates in snowflake_coordinates:
        x, y = coordinates[0], coordinates[1]
        delta_x = sd.random_number(1, 10)
        delta_y = sd.random_number(11, 20)

        x = x + delta_x
        y = y + delta_y
        center = sd.get_point(x, y)
        sd.snowflake(center=center, length=50, factor_a=0.6, factor_b=0.35, factor_c=60)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

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


