# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

while(True):
  user_vlan_number = input('Input correct VLAN number: ').strip()
  
  if user_vlan_number.isdigit() and int(user_vlan_number) > 0:
    break

ignore_words = ['mac address-table', 'Mac Addres']
raw_cam_table_filename = 'CAM_table.txt'

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
        
        if int(vlan) == int(user_vlan_number):
          print('{} {} {}'.format(vlan, mac_address, port))

