# -*- coding: utf-8 -*-
'''
Задание 6.2

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX.
Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.

Создать скрипт, который преобразует MAC-адреса в формат cisco
и добавляет их в новый список mac_cisco

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

macs = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

macs_cisco = []

for mac in macs :
    macs_cisco.append( mac.replace( ':', '.' ) )
    
print( macs )
print( macs_cisco )
