# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:
- считывались строки, в которых указаны MAC-адреса
- каждая строка, где есть MAC-адрес, должна обрабатываться таким образом,
  чтобы на стандартный поток вывода была выведена таблица вида:

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ignore_words = ['mac address-table', 'Mac Addres']
raw_cam_table_filename = argv[1].strip()
clear_cam_table_filename = argv[2].strip()

with open(raw_cam_table_filename, 'r') as raw_file, open(clear_cam_table_filename, 'w') as clean_file:
  for line_from_raw_file in raw_file:
    if not line_from_raw_file.strip().startswith('-'):
      contain_ignore_word = False

      for word in ignore_words:
        if word in line_from_raw_file.strip():
          contain_ignore_word = True
          break

      if not contain_ignore_word and len(line_from_raw_file.strip()) > 0:
        vlan, mac_address, entry_type, port = line_from_raw_file.strip().split() 
        clean_file.write('{}  {}  {}\n'.format(vlan, mac_address, port))
