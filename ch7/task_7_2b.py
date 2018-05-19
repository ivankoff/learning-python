# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы только строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore_words = ['duplex', 'alias', 'Current configuration']
src_cfg_filename = argv[1].strip()
dst_cfg_filename = argv[2].strip()

with open(src_cfg_filename, 'r') as src_cfg, open(dst_cfg_filename, 'w') as dst_cfg:
  for cfg_line in src_cfg:
    contain_ignore_word = False

    for word in ignore_words:
      if word in cfg_line.rstrip():
        contain_ignore_word = True
        break

    if not contain_ignore_word:
      dst_cfg.write(cfg_line)
