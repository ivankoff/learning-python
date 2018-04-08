# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

network_address = ( input( 'Input IPv4 network address: ' ) ).strip()
ip_address, prefix_length = network_address.split( '/' )

print_template = '''
Network:
 {0:<8} {1:<8} {2:<8} {3:<8}
 {0:0>8b} {1:0>8b} {2:0>8b} {3:0>8b}

Mask:
/{4}
 {5:<8} {6:<8} {7:<8} {8:<8}
 {5:0>8b} {6:0>8b} {7:0>8b} {8:0>8b}
'''

mask = ( '1' * int(prefix_length) + '0' * ( 32 - int(prefix_length) ) )
ip_address_octet = ip_address.split( '.' )

print( '\n' * 2 + '-' * 60 )
print( print_template.format( int( ip_address_octet[0] ),
                              int( ip_address_octet[1] ),
                              int( ip_address_octet[2] ),
                              int( ip_address_octet[3] ),
                              prefix_length,
                              int( mask[0:8],   2),
                              int( mask[8:16],  2),
                              int( mask[16:24], 2),
                              int( mask[24:],   2) ) )
print( '-' * 60 )
