# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

class_A = range( 1, 127 )
class_B = range( 128, 191 )
class_C = range( 192, 223 )
class_D = range( 224, 239 )

ip_address = ( input( 'Input IP-address (xxx.xxx.xxx.xxx) : ' ) ).strip()

# if ip_address = '0.0.0.0' -> int( ip_address.replace( '.', '' ) ) = 0
# if ip_address = '255.255.255.255' -> int( ip_address.replace( '.', '' ) ) = 255255255255
# if ip_address = '1.2.3.4' -> int( ip_address.split( '.' )[0] ) = 1 - first octet of IP-address

ip_address_first_octet_value = int( ip_address.split('.')[0] )

if int( ip_address.replace( '.', '' ) ) == 0 :
    print( 'unassigned' )
elif int( ip_address.replace( '.', '' ) ) == 255255255255 :
    print( 'local broadcast' )
elif ip_address_first_octet_value in class_A or ip_address_first_octet_value in class_B or ip_address_first_octet_value in class_C :     
    print( 'unicast' )
elif ip_address_first_octet_value in class_D :
    print( 'multicast' )
else :
    print( 'unused' )

