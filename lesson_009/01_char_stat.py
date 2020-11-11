# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile


class LetterCounter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        z_file = zipfile.ZipFile(self.file_name, 'r')
        for filename in z_file.namelist():
            z_file.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char in self.stat:
                self.stat[char] += 1
            else:
                self.stat[char] = 1

    def format(self):
        print('+---------+-----------+')
        print('|  буква  |  частота  |')
        print('+---------+-----------+')
        stat_list = list(self.stat.items())
        stat_list.sort(reverse=True, key=lambda i: i[1])
        for item in stat_list:
            if item[0].isalpha():
                print(f'|{item[0]: ^9}|{item[1]: ^11}|')


counter = LetterCounter(file_name='python_snippets/voyna-i-mir.txt.zip')
counter.collect()
counter.format()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
