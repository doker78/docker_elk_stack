...
 
# Retrieve an existing local library.
local_library_stub = content_client.LocalLibrary(my_stub_config)
local_library = local_library_stub.get(my_library_id)
 
# Specify how the local library is published, using BASIC authentication.
publish_info = library_client.PublishInfo()
publish_info.user_name = ’vcsp’ # Can omit this value; if specified, it must be ’vcsp’.
publish_info.password = ’password’
publish_info.authentication_method = library_client.PublishInfo.AuthenticationMethod.BASIC
publish_info.published = True
 
# Update the LibraryModel object retieved in step 1
# and configure it with the PublishInfo object.
local_library.publish_info = publish_info
 
# Use the LibraryModel object to update the library instance.
local_library_stub.update(library_id=my_library_id,
update_spec=local_library)