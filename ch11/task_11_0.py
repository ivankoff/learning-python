# -*- coding: utf-8 -*-

import func_11_0 as func
from sys import argv

############### program #####################################################################################

if __name__ == '__main__' :

  cfg_file_name = argv[1].strip()
  result_file_name = 'result.txt'
  
  access_dict = {}
  trunk_dict = {}
  
  access_cmd_list = []
  trunk_cmd_list = []
  
  access_dict, trunk_dict = func.get_int_vlan_map(cfg_file_name)
  access_cmd_list = func.generate_access_config(access_dict)
  trunk_cmd_list = func.generate_trunk_config(trunk_dict)
  
  file_to_write = open(result_file_name, 'w')
  
  file_to_write.writelines( [line + '\n' for line in access_cmd_list] )
  file_to_write.writelines( [line + '\n' for line in trunk_cmd_list] )
  
  file_to_write.close()
