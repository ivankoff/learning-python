# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
import argparse, ipaddress
from tabulate import tabulate

from task_12_1 import check_ip_addresses_v2, is_valid_ip

############### functions ###################################################################################
    
def check_ip_availability(in_ip_address_list):
  
  final_ip_list = []
  
  for ip in in_ip_address_list:  
    if is_valid_ip(ip_address_to_check=ip.strip()): # if ip-address looks like 10.0.0.1
      final_ip_list.append(ip.strip())
    else: #if ip-addresses looks like 10.1.1.8-10.1.1.10 or 10.1.1.8-10
      temp_list = ip.split('-')
      
      if bool( is_valid_ip(ip_address_to_check=temp_list[0].strip()) and is_valid_ip(ip_address_to_check=temp_list[1].strip()) ):
        # 10.1.1.8-10.1.1.10
        
        start_ip = ipaddress.ip_address(temp_list[0].strip())
        end_ip = ipaddress.ip_address(temp_list[1].strip())
        while start_ip <= end_ip:
          final_ip_list.append(str(start_ip))
          start_ip = start_ip + 1
          
      elif bool( is_valid_ip(ip_address_to_check=temp_list[0].strip()) and temp_list[1].isdigit() ):
        # 10.1.1.8-10
        
        start_ip = ipaddress.ip_address(temp_list[0].strip())
        '''
        if we have range of ip written as 10.1.1.8-10
        to calculate the last ip we have to calculate delta using formula: [integer] - [last octet of first ip]
        where (in our example) [integer] = 10 ( this is temp_list[1] )
        [last ocet of first ip] = 8 ( extracted using this expression int(temp_list[0].strip().split('.')[-1]) )
        '''
        end_ip = start_ip + int(temp_list[1]) - int(temp_list[0].strip().split('.')[-1])
        while start_ip <= end_ip:
          final_ip_list.append(str(start_ip))
          start_ip = start_ip + 1

  print(final_ip_list)        
  return check_ip_addresses_v2(final_ip_list)
  
def ip_table(alive_ip_list, dead_ip_list):
  table_ip_list = []
  column_headers = ['Reachable','Unreachable']
  
  '''
  make input list of the same length (equalize them)
  '''
  if len(alive_ip_list) > len(dead_ip_list):
    delta = len(alive_ip_list) - len(dead_ip_list)
    dead_ip_list = dead_ip_list + ['' for i in range(delta)]
  elif len(dead_ip_list) > len(alive_ip_list):
    delta = len(dead_ip_list) - len(alive_ip_list)
    alive_ip_list = alive_ip_list + ['' for i in range(delta)]
    
  '''
  populate table_ip_list with data for tabulate
  '''
  table_ip_list = [[alive, dead] for alive,dead in zip(alive_ip_list, dead_ip_list)]
  
  return tabulate(table_ip_list, headers=column_headers)

#############################################################################################################

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='IP-address(es) availability check script')
  parser.add_argument('filename', action='store', help='File with the list of IPs to check. One IP per string.')
  
  args = parser.parse_args()
  
  available_ip_list = []
  unavailable_ip_list = []
  
  f = open(args.filename, 'r')
  
  available_ip_list, unavailable_ip_list = check_ip_availability(in_ip_address_list=f.read().rstrip().split('\n'))
  
  f.close()
  
  print('\n' + ip_table(alive_ip_list=available_ip_list, dead_ip_list=unavailable_ip_list))
