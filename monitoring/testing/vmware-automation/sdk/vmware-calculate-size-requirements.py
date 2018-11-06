#
# calculate the size needed to store a backup image of the vCenter

from com.vmware.appliance.recovery.backup_client import Parts

 # This example assumes you have previously created a session
 # and stored the session ID in my_stub_config.

 # Issue a request to list the backup image parts.
 Parts_stub = Parts( my_stub_config )
 parts = Parts_stub.list()

 # Extract IDs of backup image parts.
 sizes = {}
 total = 0
 for part in parts :
    size = Parts_stub.get( part.id )
    sizes[part.id] = size
    total += size

 # Show the result.
 print( 'Backup image parts:' )
 for part_id in sizes.keys() :
    print( '  part {0} = {1}KB'.format( part_id, sizes[part_id] ) )
    print( 'Total size: {0}KB'.format( total ) )