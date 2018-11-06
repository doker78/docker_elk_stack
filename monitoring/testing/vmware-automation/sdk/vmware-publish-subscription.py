...
 
# Create a StorageBacking instance on a local file system.
library_backing = library_client.StorageBacking()
library_backing.type = library_client.StorageBacking.Type.OTHER
library_backing.storage_uri = ’/mnt/nfs/cls-root’
 
# Create a new SubscriptionInfo object to describe the subscription behavior.
subscription_info = library_client.SubscriptionInfo()
subscription_info.authentication_method = library_client.SubscriptionInfo.AuthenticationMethod.BASIC
subscription_info.user_name = ’libraryUser’
subscription_info.password = ’password’
subscription_info.subscription_url = ’https://www.acmecompary.com/library_inventory/lib.json’
subscription_info.automatic_sync_enabled = True
subscription_info.ssl_thumbprint = ’9B:00:3F:C4:4E:B1:F3:F9:0D:70:47:48:E7:0B:D1:A7:0E:DE:60:A5’
 
# Create a new LibraryModel object for the subscribed library.
library_model = content_client.LibraryModel()
library_model.type = content_client.LibraryModel.LibraryType.SUBSCRIBED
library_model.name = ’subscrLibrary’
 
# Attach the storage backing and the subscription info to the library model.
library_model.storage_backings = [library_backing]
library_model.subscription_info = subscription_info
 
# Create the new library instance.
idem_token = str(uuid.uuid4())
local_library_stub = content_client.LocalLibrary(my_stub_config)
library_id = local_library_stub.create(create_spec=library_model,client_token=idem_token)