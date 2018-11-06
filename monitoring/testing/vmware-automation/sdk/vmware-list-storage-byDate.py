#
#  example requests the individual data types
#  query as a composite metric for all storage used by Alarms, Statistics, Events, and Tasks in the vCenter Server instance

from com.vmware import appliance_client
import datetime

# This example assumes you have previously created a session
# and stored the session ID in my_stub_config.

# Prepare request for chosen data types.
req = appliance_client.Monitoring.MonitoredItemDataRequest()
req.interval = appliance_client.Monitoring.IntervalType.MINUTES30
req.function = appliance_client.Monitoring.FunctionType.MAX
d_now = datetime.datetime.utcnow()
req.start_time = d_now - datetime.timedelta( minutes=30 )
req.end_time = d_now
mon = {'storage.totalsize.directory.vcdb_hourly_stats' :
         'Hourly stats',
       'storage.totalsize.directory.vcdb_daily_stats' :
         'Daily stats',
       'storage.totalsize.directory.vcdb_monthly_stats' :
         'Monthly stats',
       'storage.totalsize.directory.vcdb_yearly_stats' :
         'Yearly stats',
       'storage.totalsize.directory.vcdb_events' :
         'Events',
       'storage.totalsize.directory.vcdb_alarms' :
         'Alarms',
       'storage.totalsize.directory.vcdb_tasks' :
         'Tasks'}

req.names = []
for item in mon.keys() :
   req.names.append( item )

# Issue request.
Monitoring_stub = appliance_client.Monitoring( my_stub_config )
resp = Monitoring_stub.query( req )

# Assemble data from response.
out = {}
for metric in resp :
  # Discard empty data points:
  stat = ''
  while (stat == '') :
    stat = metric.data.pop()
  stat = int(stat)
  out[mon[metric.name]] = stat

# Format and print statistics.
for label in sorted( out.keys() ) :
  print( '{0:15s}: {1:8d} KB'.format( label, out[label] ) )