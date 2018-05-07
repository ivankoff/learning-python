# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


class_A = range(  1, 128)
class_B = range(128, 192)
class_C = range(192, 224)
class_D = range(224, 240)

octet_valid_range = range(0, 256)

while True :
    ip_address = ( input( 'Input IP-address (xxx.xxx.xxx.xxx) : ' ) ).strip()

    try :
        ip_address_octet = ip_address.split( '.' )
        
        if len( ip_address_octet ) != 4 :
            raise ValueError( 'Incorrect length of the given IPv4 address!' )
            
        for index in range(4) :
            ip_address_octet[index] = int( ip_address_octet[index] )
            
            if ip_address_octet[index] not in octet_valid_range :
                raise ValueError( 'Octet value out of of valid range!' )

    except ( ValueError, IndexError ) :
        print( 'Incorrect IPv4 address' )
    
    else :
        break

# if ip_address = '0.0.0.0' -> int( ip_address.replace( '.', '' ) ) = 0
# if ip_address = '255.255.255.255' -> int( ip_address.replace( '.', '' ) ) = 255255255255

if int( ip_address.replace( '.', '' ) ) == 0 :
    print( 'unassigned' )
elif int( ip_address.replace( '.', '' ) ) == 255255255255 :
    print( 'local broadcast' )
elif ip_address_octet[0] in class_A or ip_address_octet[0] in class_B or ip_address_octet[0] in class_C :     
    print( 'unicast' )
elif ip_address_octet[0] in class_D :
    print( 'multicast' )
else :
    print( 'unused' )
