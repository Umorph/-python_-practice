# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7

paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

if paper_x <= envelop_x and paper_y <= envelop_y:
    print('Письмо поместится в конверт')
elif paper_y <= envelop_x and paper_x <= envelop_y:
    print("Письмо поместится в конверт")
else:
    print('Письмо не поместится в конверт')

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

hole_x, hole_y = 8, 9
brick_coordinates = {
    'brick_x': [11, 11, 10, 10, 2, 2, 3, 3, 6, 6, 5, 5, 11, 11, 6, 6, 3, 3],
    'brick_y': [10, 2, 11, 2, 10, 11, 5, 6, 3, 5, 6, 3, 3, 6, 11, 3, 6, 11],
    'brick_z': [2, 10, 2, 11, 11, 10, 6, 5, 5, 3, 3, 6, 6, 3, 3, 11, 11, 6]
}

brick_x = brick_coordinates.get('brick_x')
brick_y = brick_coordinates.get('brick_y')
brick_z = brick_coordinates.get('brick_z')
# Проверяем верность ввенных данных
if len(brick_x) == len(brick_y) and len(brick_y) == len(brick_z):
    i = 0
    while i <= len(brick_x):
        current_x = brick_x[i]
        current_y = brick_y[i]
        current_z = brick_z[i]
        # Проверяем грань XY
        print('Brick ', i, 'checking')
        if current_x <= hole_x and current_y <= hole_y:
            print('Pass XY x to x')
        elif current_y <= hole_x and current_x <= hole_y:
            print('pass XY y to x')
        else:
            # Проверяем грань YZ
            if current_y <= hole_x and current_z <= hole_y:
                print('Pass YZ y to x')
            elif current_z <= hole_x and current_y <= hole_y:
                print('pass YZ z to x')
            else:
                # Проверяем по XZ
                if current_x <= hole_x and current_z <= hole_y:
                    print('pass XZ x to x')
                elif current_z <= hole_x and current_x <= hole_y:
                    print('pass XZ z to x')
                else:
                    print('Brick ', i, 'not pass')
        i += 1
else:
    print('Проверьте правильность введенный данных размером кирпичей')