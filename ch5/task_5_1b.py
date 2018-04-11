# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

network_address = argv[1].strip()
ip_address, prefix_length = network_address.split( '/' )

if int( prefix_length ) > 32 :
    print( ' Invalid network prefix! Must be less or equal 32. ' )
else :
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
    
    for i in range( 4 ) :   # Convert octet from decimal to binary ( for example: 3 -> 00000011 )
        ip_address_octet[i] = '{:0>8b}'.format( int( ip_address_octet[i] ) )
    
    temp_octet = ''
    
    if int( mask[0:8], 2) < 255 :
        for i in range( 8 ) :
            if int( mask[i] ) == 0 :
                temp_octet = temp_octet + '0'
            else :
                temp_octet = temp_octet + ip_address_octet[0][i]
                
        ip_address_octet[0] = temp_octet
        temp_octet = ''
                
    if int( mask[8:16], 2) < 255 :
        for i in range( 8 ) :
            if int( mask[i + 8] ) == 0 :
                temp_octet = temp_octet + '0'
            else :
                temp_octet = temp_octet + ip_address_octet[1][i]

        ip_address_octet[1] = temp_octet
        temp_octet = ''
                
    if int( mask[16:24], 2) < 255 :
        for i in range( 8 ) :
            if int( mask[i + 16] ) == 0 :
                temp_octet = temp_octet + '0'
            else :
                temp_octet = temp_octet + ip_address_octet[2][i]

        ip_address_octet[2] = temp_octet
        temp_octet = ''
                
    if int( mask[24:], 2) < 255 :
        for i in range( 8 ) :
            if int( mask[i + 24] ) == 0 :
                temp_octet = temp_octet + '0'
            else :
                temp_octet = temp_octet + ip_address_octet[3][i]

        ip_address_octet[3] = temp_octet

    print( '\n' * 2 + '-' * 60 )
    print( print_template.format( int( ip_address_octet[0], 2),
                                  int( ip_address_octet[1], 2),
                                  int( ip_address_octet[2], 2),
                                  int( ip_address_octet[3], 2),
                                  prefix_length,
                                  int( mask[0:8],   2),
                                  int( mask[8:16],  2),
                                  int( mask[16:24], 2),
                                  int( mask[24:],   2) ) )
    print( '-' * 60 )
