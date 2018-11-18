# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''
import argparse
import ipaddress

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
  
  print(available_ip_list)
  print('\n' + '='*100 + '\n')
  print(unavailable_ip_list)
