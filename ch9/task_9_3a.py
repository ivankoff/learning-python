# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
############### functions ###################################################################################

def get_int_vlan_map(in_cfg_file):
    access_intf_dict = {}
    trunk_intf_dict = {}
    
    with open(in_cfg_file, 'r') as cfg_file:
      
      for cfg_line in cfg_file:
      
        if cfg_line.strip().startswith('interface FastEthernet'):
          _, intf = cfg_line.strip().split()
          
        if cfg_line.strip().startswith('switchport mode access'):
          access_intf_dict[intf] = 1
        
        if cfg_line.strip().startswith('switchport access vlan'):
          *other, vlan_num = cfg_line.strip().split()
          access_intf_dict[intf] = int(vlan_num)
          
        if cfg_line.strip().startswith('switchport trunk allowed vlan'):
          *other, vlan = cfg_line.strip().split()
          trunk_intf_dict[intf] = [int(vlan_num) for vlan_num in vlan.split(',')]
          
    return access_intf_dict, trunk_intf_dict

############### program #####################################################################################

access_dict = {}
trunk_dict = {}

access_dict, trunk_dict = get_int_vlan_map('config_sw2.txt')

print(access_dict)
print('')
print(trunk_dict)
