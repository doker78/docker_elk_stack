#
# this example retrieve in 30 min interval for 2 hours period

from com.vmware import appliance_client
import datetime

# This example assumes you have previously created a session
# and stored the session ID in my_stub_config.

# Issue request for core inventory and 'SEAT' (stats, events, & alarms) usage.
req = appliance_client.Monitoring.MonitoredItemDataRequest()
req.names = ['storage.used.filesystem.vcdb_core_inventory',
             'storage.used.filesystem.vcdb_seat']
req.interval = appliance_client.Monitoring.IntervalType.MINUTES30
req.function = appliance_client.Monitoring.FunctionType.MAX
d_now = datetime.datetime.utcnow()
 req.start_time = d_now - datetime.timedelta( minutes=135 )
 req.end_time = d_now - datetime.timedelta( minutes=15 )
 Monitoring_stub = appliance_client.Monitoring( my_stub_config )
 resp = Monitoring_stub.query( req )

 # Extract resulting arrays.
 core_sizes = resp[0].data
 seat_sizes = resp[1].data
 # Remove empty data points:
 core_sizes = filter( (lambda x: x != ''), core_sizes )
 seat_sizes = filter( (lambda x: x != ''), seat_sizes )

 # Add the usage stats for each interval, and display maximum usage.
 highest = max( map( (lambda a,b: int(a) + int(b)),
                      core_sizes, seat_sizes ) )
 print( 'vCenter database inventory + stats, events, alarms, tasks:' +
         ' (max) size = {0} KB'.format( highest ) )