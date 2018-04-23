# -*- coding: utf-8 -*-
'''
Задание 5.4

Найти индекс последнего вхождения элемента.

Например, для списка num_list, число 10 последний раз встречается с индексом 4;
в списке word_list, слово 'ruby' последний раз встречается с индексом 6.

Сделать решение общим (то есть, не привязываться к конкретному элементу в конкретном списке) и
проверить на двух списках, которые указаны и на разных элементах.

Для этого надо запросить у пользователя сначала ввод числа из списка num_list и затем вывести
индекс его последнего появления в списке. А затем аналогично для списка word_list.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

# Hack: num_list[::-1] - reverse the list

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = [
    'python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl'
]

list_element = int( input( 'Select element from the number list ' + str( num_list ) + ' : ' ) )
last_appearance_index = len( num_list ) - num_list[::-1].index( list_element ) - 1

print( 'Index of the last appearance: ' + str( last_appearance_index ) + '\n' )

list_element = ( input( 'Select element from the word list ' + str( word_list ) + ' : ' ) ).strip()
last_appearance_index = len( word_list ) - word_list[::-1].index( list_element ) - 1

print( 'Index of the last appearance: ' + str( last_appearance_index ) )
