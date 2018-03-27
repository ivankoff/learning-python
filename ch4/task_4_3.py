# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print( 'Before\n\t' + CONFIG )

vlans = list()

for vlan in CONFIG.strip().replace(' ',',').split(','):
    if vlan.isdigit():
        vlans.append( vlan )

print( 'After\n\t' + str( vlans ) )
