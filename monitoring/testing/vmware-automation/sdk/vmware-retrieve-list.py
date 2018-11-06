...
 
library_stub = content_client.Library(my_stub_config)
libraries = library_stub.list()
print(’List of all library identifiers:’)
for library_id in library_ids :
  library = library_stub.get(library_id)
  print(’Library ID {}: {}’.format(library_id, library.name))