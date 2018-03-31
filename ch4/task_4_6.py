# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
route_info_template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''

route_info = ospf_route.strip().replace( 'O', 'OSPF' ).replace( '[', '' ).replace( ']', '' ).replace( 'via', '' ).replace( ',', '' ).split()

print( route_info_template.format( route_info[0],  route_info[1], route_info[2], route_info[3], route_info[4], route_info[5] ) )
