# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию скрипта задания 9.2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

############### functions ###################################################################################

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''
    return_cmd_dict = {intf: [] for intf in trunk.keys()}
    
    trunk_template = [
                     'switchport trunk encapsulation dot1q',
                     'switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan'
                     ]

    for intf in trunk.keys():
      vlan_list = [str(vlan) for vlan in trunk[intf]]
      
      for cmd in trunk_template:
        if cmd.endswith('trunk allowed vlan'):
          return_cmd_dict[intf].append('{} {}'.format(cmd, ','.join(vlan_list)))
        else:
          return_cmd_dict[intf].append(cmd)
          
    return return_cmd_dict

############### program #####################################################################################

trunk_dict = {
              'FastEthernet0/1': [10, 20, 30],
              'FastEthernet0/2': [11, 30],
              'FastEthernet0/4': [17]
             }

result_cmd_dict = {}
result_cmd_dict = generate_trunk_config(trunk_dict)

print(result_cmd_dict)
