# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore_words = ['duplex', 'alias', 'Current configuration']
config_file_name = argv[1].strip()
file_mode = 'r'

with open( config_file_name, file_mode ) as config_file :
    for config_line in config_file :
        if not config_line.startswith( '!' ) :
            contain_ignore_word = False
            
            for word in ignore_words :
                if word in config_line.rstrip() :
                    contain_ignore_word = True
                    break

            if not contain_ignore_word :
                print( config_line.rstrip() )

