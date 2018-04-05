access_template = [ 'switchport mode access',
                    'switchport access vlan {}',
                    'switchport nonegotiate',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable' ]

target_interface = input( 'Input interface name: ' )
target_vlan = input( 'Input vlan number: ' ) 

print('\n' + '=' * 30 )
print( 'interface {}'.format( target_interface.strip() ) )
print( '\n'.join( access_template ).format( target_vlan.strip() ) )
