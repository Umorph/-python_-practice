# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile as zipfile
import re
from cprint import cprint
from pprint import pprint


class ParserEngine:
    def __init__(self, input_file, output_file):
        self.input_path = input_file
        self.output_path = output_file
        self.output_string = ''
        self.line_content = {
            'year': '',
            'month': '',
            'day': '',
            'hour': '',
            'minute': '',
            'second': '',
            'millisecond': '',
            'status': ''
        }
        self.prev_line = {
            'year': '',
            'month': '',
            'day': '',
            'hour': '',
            'minute': ''
        }
        # [2018-05-17 01:57] 1234
        self.reference = 0
        self.bug_count = 0
        self._first_line = True

    def unzip(self):
        filename = ''
        zipped_file = zipfile.ZipFile(self.input_path, 'r')
        for filename in zipped_file.namelist():
            zipped_file.extract(filename)
        self.input_path = filename

    def read_the_file(self):
        line_number = 0
        with open(self.input_path, 'r', encoding='utf-8') as file:
            for line in file:
                print('--------------------------------------------')
                cprint(f'СТРОКА №{line_number} - {line[0:-1]}', c="m")
                self.parse_current_line(line=line)
                self.check_current_line()
                line_number += 1

    def parse_current_line(self, line):
        result = re.findall(r'\w+', line)
        self.line_content['year'] = result[0]
        self.line_content['month'] = result[1]
        self.line_content['day'] = result[2]
        self.line_content['hour'] = result[3]
        self.line_content['minute'] = result[4]
        self.line_content['second'] = result[5]
        self.line_content['millisecond'] = result[6]
        self.line_content['status'] = result[7]
        pprint(self.line_content)

    def check_current_line(self):
        current_minute = self.line_content['minute']
        cprint(f'Текущая минута - {current_minute}, образец для проверки - {self.reference}, начинаю проверку', c='b')
        if current_minute == self.reference:
            cprint('Та же минута, перехожу к проверке статуса', c='g')
            if self.line_content['status'] == 'OK':
                cprint('Статус лога - ОК, приступаю к следующей строке', c='g')
            elif self.line_content['status'] == 'NOK':
                cprint('Статус лога - NOK, работаю', c='y')
                self.bug_count += 1
                cprint(f'Обновил количество багов, текущее значение - {self.bug_count}, приступаю к следующей строке',
                       c='g')
            else:
                cprint('Не могу прочитать статус лога, что-то пошло не так...', c='r')

        elif current_minute != self.reference:
            if self._first_line:
                cprint('Кажется это первая строка, пропускаю итерацию', c='b')
                self._first_line = False
            else:
                cprint('Обнаружена новая минута, подготавливаю данные для выхода', c='y')
                self.output_string = '[' + self.prev_line['year'] + '-' + self.prev_line['month'] + '-' + \
                                     self.prev_line['day'] + ' ' + self.prev_line['hour'] + ':' + \
                                     self.prev_line['minute'] + ']' + ' ' + str(self.bug_count) + '\n'
                cprint(f'Строка для вывода - {self.output_string}, начинаю экспорт')
                self.write_to_file()
                cprint('Вывод завершен, актуализирую переменные', c='g')
            self.bug_count = 0
            self.reference = self.line_content['minute']
            cprint(f'Новые данные: Образец - {self.reference}, количество ошибок - {self.bug_count}', c='b')
            cprint('Приступаю к проверке статуса', c='g')
            if self.line_content['status'] == 'OK':
                cprint('Статус лога - ОК, приступаю к следующей строке', c='g')
            elif self.line_content['status'] == 'NOK':
                cprint('Статус лога - NOK, работаю', c='y')
                self.bug_count += 1
                cprint(
                    f'Обновил количество багов, текущее значение - {self.bug_count}, приступаю к следующей строке',
                    c='g')
            else:
                cprint('Не могу прочитать статус лога, что-то пошло не так...', c='r')

        else:
            cprint('Something goes wrong', c='r')
        self._remember_prev_line()

    def write_to_file(self):
        with open(self.output_path, 'a', encoding='utf-8') as output:
            output.write(self.output_string)

    def _remember_prev_line(self):
        self.prev_line['year'] = self.line_content['year']
        self.prev_line['month'] = self.line_content['month']
        self.prev_line['day'] = self.line_content['day']
        self.prev_line['hour'] = self.line_content['hour']
        self.prev_line['minute'] = self.line_content['minute']

    def parse(self):
        if self.input_path.endswith('.zip'):
            self.unzip()
        self.read_the_file()


my_parser = ParserEngine(input_file='events.txt', output_file='output.txt')
my_parser.parse()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
