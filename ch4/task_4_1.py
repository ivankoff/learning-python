# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку NAT таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

NAT = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
print( 'Before\n\t' + NAT )

NAT = NAT.replace('Fast', 'Gigabit')
print( 'After\n\t' + NAT )