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

# TODO здесь ваш код

class LogParser:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def parse_file(self):
        with open(self.input_file, 'r', encoding='utf8') as log_file:
            sorting_minute = 0
            nok_counter = 0
            for line in log_file:
                current_minute = line[15:17]
                current_status = line[29:31]
                if current_minute == sorting_minute:
                    if current_status == 'OK':
                        print('current status is ok')
                    elif current_status == 'NO':
                        print('current status is nok')
                        nok_counter += 1
                    else:
                        print('cant understand current status')
                else:
                    sorting_minute = current_minute
                    with open(self.output_file, 'a', encoding='utf8') as output_file:
                        output_file.write(str(nok_counter))
                        output_file.write(' ')
                        nok_counter = 0
                    if current_status == 'OK':
                        print('current status is ok')
                    elif current_status == 'NO':
                        print('current status is nok')
                        nok_counter += 1
                    else:
                        print('cant understand current status')


my_log_parser = LogParser(input_file='events.txt', output_file='output.txt')
my_log_parser.parse_file()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
