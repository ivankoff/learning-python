# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv

############### functions ###################################################################################

def parse_cdp_neighbors(output_from_file_as_a_string) :

  local_device_name = ''
  next_line_is_data = False
  output_from_file = []
  
  return_result_dict = {}
  
  output_from_file =[item.strip() for item in output_from_file_as_a_string.split('\n') if item.strip()] 
      
  for line in output_from_file:
    if 'show cdp neig' in line :
      local_device_name, *rest = line.split('>')

    if next_line_is_data :
      result_data_list = [item.strip() for item in line.split('   ') if item]
      neighbor_device_name, local_intf, *rest, neighbor_intf = result_data_list

      return_result_dict[tuple( [local_device_name, local_intf] )] = tuple( [neighbor_device_name, neighbor_intf] )

    if 'Device ID' in line :
      next_line_is_data = True

  return return_result_dict

#############################################################################################################

if __name__ == '__main__' :
  in_file_name = argv[1].strip()
  result_dict = {}
  
  f = open(in_file_name, 'r')
  result_dict = parse_cdp_neighbors(f.read())
  f.close()
  
  print(result_dict)
