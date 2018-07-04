# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

############### functions ###################################################################################
'''
def get_int_vlan_map(in_cfg_file):
    #
    # Returns two dictionaries
    # first: interfaces in access mode (as keys) with list of their configuration commands (as values)
    # second: interfaces in trunk mode (as keys) with list of their configuration commands (as values)
    #
    access_intf_dict = {}
    trunk_intf_dict = {}
    intf_cfg_cmd = []
    
    reading_intf_cfg = False
    intf_mode = ''  # 'trunk' or 'access'
    
    with open(in_cfg_file, 'r') as cfg_file:
      for cfg_line in cfg_file:
        
        if reading_intf_cfg and not cfg_line.strip().startswith('!'):
          intf_cfg_cmd.append(cfg_line.strip())
          
          if cfg_line.strip().endswith('mode trunk'):
            intf_mode = 'trunk'
            
          if cfg_line.strip().endswith('mode access'):
            intf_mode = 'access'
                  
        if reading_intf_cfg and cfg_line.strip().startswith('!'):
          if intf_mode == 'access':
            access_intf_dict[intf] = []
            access_intf_dict[intf].extend(intf_cfg_cmd)
            
          if intf_mode == 'trunk':
            trunk_intf_dict[intf] = []
            trunk_intf_dict[intf].extend(intf_cfg_cmd)
          
          intf_cfg_cmd.clear()
          reading_intf_cfg = False
          intf_mode = ''

        if cfg_line.strip().startswith('interface FastEthernet'):
          _, intf = cfg_line.strip().split()
          reading_intf_cfg = True
          
    return access_intf_dict, trunk_intf_dict
'''

def get_int_vlan_map(in_cfg_file):
    access_intf_dict = {}
    trunk_intf_dict = {}
    
    with open(in_cfg_file, 'r') as cfg_file:
      
      for cfg_line in cfg_file:
      
        if cfg_line.strip().startswith('interface FastEthernet'):
          _, intf = cfg_line.strip().split()
          
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

access_dict, trunk_dict = get_int_vlan_map('config_sw1.txt')

print(access_dict)
print('')
print(trunk_dict)
