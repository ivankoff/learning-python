# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlans1 = set()
vlans2 = set()
vlans  = list()

for vlan in command1.strip().replace( ' ', ',' ).split( ',' ) :
    if vlan.isdigit() :
        vlans1.add( int( vlan ) )

for vlan in command2.strip().replace( ' ', ',' ).split( ',' ) :
    if vlan.isdigit() :
        vlans2.add( int( vlan ) )

vlans = list( vlans1.intersection( vlans2 ) )

print( vlans )
