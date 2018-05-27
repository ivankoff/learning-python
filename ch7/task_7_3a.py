# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ignore_words = ['mac address-table', 'Mac Addres']
raw_cam_table_filename = argv[1].strip()
cam_table_cleared = list()
vlan_list = set()

with open(raw_cam_table_filename, 'r') as raw_file:
  for line_from_raw_file in raw_file:
    if not line_from_raw_file.strip().startswith('-'):
      contain_ignore_word = False

      for word in ignore_words:
        if word in line_from_raw_file.strip():
          contain_ignore_word = True
          break

      if not contain_ignore_word and len(line_from_raw_file.strip()) > 0:
        vlan, mac_address, entry_type, port = line_from_raw_file.strip().split() 
        cam_table_cleared.append([int(vlan), mac_address, port])
        vlan_list.add(int(vlan))

for vlan in sorted(vlan_list):
  for row in cam_table_cleared:
    if row[0] == vlan:
      print('{} {} {}'.format(row[0], row[1], row[2]))
