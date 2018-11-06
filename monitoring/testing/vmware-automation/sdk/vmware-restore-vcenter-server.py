#
# example uses the following global variables.
# ■ my_vcsa_hostname
# ■ my_vcsa_username
# ■ my_vcsa_password
# ■ my_backup_name
# ■ my_storage_server
# ■ my_scp_user
# ■ my_scp_password
# ■ my_backup_folder

import requests
 from vmware.vapi.lib.connect import get_requests_connector
 from vmware.vapi.security.user_password import create_user_password_security_context
 from vmware.vapi.stdlib.client.factories import StubConfigurationFactory
 from com.vmware.appliance.recovery.restore_client import (Job)
 import time

 # Create a session object in the client.
 session = requests.Session()

 # For development environment only, suppress server certificate checking.
 session.verify = False
 from requests.packages.urllib3 import disable_warnings
 from requests.packages.urllib3.exceptions import InsecureRequestWarning
 disable_warnings(InsecureRequestWarning)

 # Create a connection to Appliance port 5480.
 local_url = 'https://%s:5480/api' % my_vcsa_hostname
 connector = get_requests_connector(session=session, url=local_url)

 # Add username/password security context to the connector.
 basic_context = create_user_password_security_context(my_vcsa_username, my_vcsa_password)
 connector.set_security_context(basic_context)

 # Create a stub configuration by using the username-password security context.
 local_stub_config = StubConfigurationFactory.new_std_configuration(connector)

 # Create a restore request object.
 req = Job.RestoreRequest()
 req.location_type = Job.LocationType.SCP
 req.location = my_storage_server + ':/home/scpuser/' + my_backup_folder + '/' + my_backup_name
 req.location_user = my_scp_user
 req.location_password = my_scp_password

 # Issue a request to start the restore operation.
 restore_job = Job( local_stub_config )
 job_status = restore_job.create( req )

 # Monitor progress of the job until it is complete.
 while (job_status.state == Job.BackupRestoreProcessState.INPROGRESS) :
     print( 'Restore job state: {} ({}%)'.format( job_status.state, 
 job_status.progress ) )
     time.sleep( 10 )
     job_status = restore_job.get()

 # Report job completion.
 print( 'Restore job completion status: {}'.format( job_status.state) )