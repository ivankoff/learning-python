# -*- coding: utf-8 -*-

############### functions ###################################################################################
'''
Функции из заданий 9.1а, 9.2 и 9.3а
'''

def generate_access_config(access, psecurity = False):
    '''
    из задания 9.1а
    
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''

    result_cmd_list = []
    
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
      result_cmd_list.append('interface {}'.format(intf))
    
      for cmd in access_template:
        if cmd.endswith('access vlan'):
          result_cmd_list.append(' {} {}'.format(cmd, vlan_num))
        else:
          result_cmd_list.append(' {}'.format(cmd))
          
      if psecurity:
        for cmd in port_security:
          result_cmd_list.append(cmd)

      result_cmd_list.append('!')

    return result_cmd_list

    
def generate_trunk_config(trunk):
    '''
    из задания 9.2а
    
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
          return_cmd_list.append(' {} {}'.format(cmd, ','.join(vlan_list)))
        else:
          return_cmd_list.append(' {}'.format(cmd))
      
      return_cmd_list.append('!')
          
    return return_cmd_list
    

def get_int_vlan_map(in_cfg_file):
    '''
    из задания 9.3а
    '''
    
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

#############################################################################################################