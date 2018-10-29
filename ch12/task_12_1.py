# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess
import ipaddress
import argparse

from sys import argv

############### functions ###################################################################################

def is_valid_ip(ip_address_to_check):
  try:
    ipaddress.ip_address(ip_address_to_check)
    return True
  except ValueError:
    return False

def check_ip_addresses(in_ip_address_list):
  '''
  Если код возврата (returncode) после выполнения subprocess.run
  равен 0, то хост в списке good_ip_list, если 1 - то в bad_ip_list
  '''
  good_ip_list = []
  bad_ip_list = []
  
  ping_count = 1
  
  for ip in in_ip_address_list:
    if is_valid_ip(ip_address_to_check=ip):
      reply = subprocess.run('ping -n {count} {host}'.format(count=int(ping_count), host=str(ip)),
                             stdout=subprocess.DEVNULL)
      
      if reply.returncode == 0:
        good_ip_list.append(ip)
        
      if reply.returncode == 1:
        bad_ip_list.append(ip)

  return good_ip_list, bad_ip_list
  
def check_ip_addresses_v2(in_ip_address_list):
  '''
  Если на 3 icmp echo requests пришло 3 icmp echo replies,
  то хост считается доступным, в противном случае нет
  '''
  good_ip_list = []
  bad_ip_list = []
  
  ping_count = 3
  
  start_pattern = ': Sent ='
  end_pattern = ', Lost ='
  
  for ip in in_ip_address_list:
    if is_valid_ip(ip_address_to_check=ip):
      reply = subprocess.run('ping -n {count} {host}'.format(count=int(ping_count), host=str(ip)),
                             stdout=subprocess.PIPE)
                             
      decoded_reply = reply.stdout.decode('utf-8')
      '''
      Вырежем из decoded_reply кусок строки который содержит
      статистику отправленных запросов и полученных ответов
      это что-то вида:
       Packets: Sent = 15, Received = 15, Lost = 0 (0% loss)
      
      и извлекём из неё необходимую информацию для анализа
      '''
      decoded_reply = decoded_reply[decoded_reply.find(start_pattern) + len(start_pattern):decoded_reply.find(end_pattern)]
      decoded_reply = decoded_reply.replace(',', '').strip()
      
      sent = int(decoded_reply.split()[0])
      received = int(decoded_reply.split()[-1])
      
      if sent == received:
        good_ip_list.append(ip)
      else:
        bad_ip_list.append(ip)
      
  
  return good_ip_list, bad_ip_list

#############################################################################################################

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='IP-address(es) availability check script')
  parser.add_argument('filename', action='store', help='File with the list of IPs to check. One IP per string.')
  
  args = parser.parse_args()
  
  available_ip_list = []
  unavailable_ip_list = []
  
  f = open(args.filename, 'r')
  
#  available_ip_list, unavailable_ip_list = check_ip_addresses(in_ip_address_list=f.read().rstrip().split('\n'))
  available_ip_list, unavailable_ip_list = check_ip_addresses_v2(in_ip_address_list=f.read().rstrip().split('\n'))
  
  f.close()
  
  print(available_ip_list)
  print('\n' + '='*100 + '\n')
  print(unavailable_ip_list)
