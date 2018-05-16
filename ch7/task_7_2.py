# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv

config_file_name = argv[1].strip()
file_mode = 'r'

with open( config_file_name, file_mode ) as config_file :
    for config_line in config_file :
        if not config_line.startswith( '!' ) :
            print( config_line.rstrip() )
            
