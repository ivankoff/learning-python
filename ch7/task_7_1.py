# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

file_name = 'ospf.txt'
file_mode = 'r'

route_info_template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}'''

with open( file_name, file_mode) as file_handle :
    for line in file_handle :
        route_info = line.strip().replace( 'O', 'OSPF' ).replace( '[', '' ).replace( ']', '' ).replace( 'via', '' ).replace( ',', '' ).split()
        print( route_info_template.format( route_info[0],  route_info[1], route_info[2], route_info[3], route_info[4], route_info[5] ) )

