...
 
# Create a FindSpec object to specify your search criteria.
find_spec = content_client.Library.FindSpec()
find_spec.name = ’AcmeLibrary’
find_spec.type = content_client.LibraryModel.LibraryType.LOCAL
 
# Invoke the find() function by using the FindSpec instance.
library_stub = content_client.Library(my_stub_config)
library_ids = library_stub.find(find_spec)