# -*- coding: utf-8 -*-
'''
Задание 9.1b

Сделать копию скрипта задания 9.1a.

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/12'
    - значения: список команд, который надо выполнить на этом интерфейсе:
                          ['switchport mode access',
                           'switchport access vlan 10',
                           'switchport nonegotiate',
                           'spanning-tree portfast',
                           'spanning-tree bpduguard enable']


Проверить работу функции на примере словаря access_dict,
с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
############### functions ###################################################################################

def generate_access_config(access, psecurity = False):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Функция возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''

    result_cmd_dict = {intf: [] for intf in access.keys()}

    access_template = [
                      'switchport mode access',
                      'switchport access vlan',
                      'switchport nonegotiate',
                      'spanning-tree portfast',
                      'spanning-tree bpduguard enable'
                      ]

    port_security = [
                    'switchport port-security maximum 2',
                    'switchport port-security violation restrict',
                    'switchport port-security'
                    ]

    for intf, vlan_num in access.items():
    
      for cmd in access_template:
        if cmd.endswith('access vlan'):
          result_cmd_dict[intf].append('{} {}'.format(cmd, vlan_num))
        else:
          result_cmd_dict[intf].append(cmd)
          
      if psecurity:
        for cmd in port_security:
          result_cmd_dict[intf].append(cmd)

    return result_cmd_dict

############### program #####################################################################################

access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

access_config_dict = {}

access_config_dict = generate_access_config(access_dict)
print(access_config_dict)

print('')
access_config_dict.clear()

access_config_dict = generate_access_config(access_dict, True)
print(access_config_dict)
