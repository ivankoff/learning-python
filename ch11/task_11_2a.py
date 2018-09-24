# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

from sys import argv
from task_11_1 import parse_cdp_neighbors
from draw_network_graph import draw_topology

if __name__ == '__main__' :
  file_list = ['sh_cdp_n_sw1.txt',
               'sh_cdp_n_r1.txt',
               'sh_cdp_n_r2.txt',
               'sh_cdp_n_r3.txt']

  dict_from_file = {}
  result_dict = {}
  
  for file in file_list:
    f = open(file, 'r')
    
    dict_from_file = parse_cdp_neighbors(f.read())
    for key, value in dict_from_file.items() :
      '''
      Если у нас в словаре уже есть ключ равный значению, то значит что это дублирующая связь.
      Т.е. на этом порту уже линк с каким-то сетевым устройством и эту связь мы добавлять не будем
      А если нет, то добавляем
      '''
      if not bool(result_dict.get(value)) :      
        result_dict.update({key:value})
    
    dict_from_file.clear()
    f.close()
  
  draw_topology(result_dict)
