# -*- coding: utf-8 -*-
'''
Задание 9.2

Создать функцию, которая генерирует конфигурацию для trunk-портов.

Параметр trunk - это словарь trunk-портов.

Словарь trunk имеет такой формат (тестовый словарь trunk_dict уже создан):
    { 'FastEthernet0/1':[10,20],
      'FastEthernet0/2':[11,30],
      'FastEthernet0/4':[17] }

Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_template.
В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_dict.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

############### functions ###################################################################################

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов, для которых необходимо сгенерировать конфигурацию

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''
    return_cmd_list = []
    
    trunk_template = [
                     'switchport trunk encapsulation dot1q',
                     'switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan'
                     ]
                     
    for intf in trunk.keys():
      vlan_list = [str(vlan) for vlan in trunk[intf]]
      
      return_cmd_list.append('interface {}'.format(intf))
      
      for cmd in trunk_template:
        if cmd.endswith('trunk allowed vlan'):
          return_cmd_list.append('{} {}'.format(cmd, ','.join(vlan_list)))
        else:
          return_cmd_list.append(cmd)
          
    return return_cmd_list

############### program #####################################################################################

trunk_dict = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

result_cmd_list = []
result_cmd_list = generate_trunk_config(trunk_dict)

print(result_cmd_list)
'''
############### formatted result output #####################################################################
for cmd in result_cmd_list:
  if cmd.startswith('interface'):
    print(cmd)
  else:
    print('  {}'.format(cmd))
'''
