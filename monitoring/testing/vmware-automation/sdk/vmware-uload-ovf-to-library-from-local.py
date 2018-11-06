...
 
# 1 - Create an empty library item to describe the VM/VApp.
item_model = library_client.ItemModel()
item_model.name = “ubuntu-vm”
item_model.description = “ubuntu 7.0”
item_model.library_id = my_library_id
item_model.type = “ovf”
client_token = str(uuid.uuid4())
item_stub = library_client.Item(my_stub_config)
item_id = item_stub.create(create_spec=item_model, client_token=client_token)
 
# 2 - Create an update session.
update_session_model = item_client.UpdateSessionModel()
update_session_model.library_item_id = item_id
client_token = str(uuid.uuid4())
update_session_stub = update_session_client.UpdateSession(my_stub_config)
session_id = update_session_stub.create(create_spec=update_session_model, client_token=client_token)
 
try :
  # 3 - Create a file spec for the OVF envelope file.
  file_spec = update_session_client.AddSpec()
  file_spec.name = “ubuntu.ovf”
  file_spec.source_type = update_session_client.File.SourceType.PUSH
 
  # 4 - Link the OVF file spec to the update session.
  update_file_stub = update_session_client.File(my_stub_config)
  file_info = update_file_stub.File.add(update_session_id=session_id, file_spec=file_spec)
  upload_uri = file_info.upload_endpoint.uri
 
  # 5 - Use HTTP library to push the file, out of band.
  file_name = “/medias/vms/ubuntu.ovf”
  host = urlparse.urlsplit(upload_uri)
  connection = httplib.HTTPConnection(host.netloc)
  with open(file_name, “rb”) as f :
    connection.request(“PUT”, upload_uri, f)
 
  # 6 - Create a file spec for the VMDK file.
  file_spec = update_session_client.AddSpec()
  file_spec.name = “ubuntu_disk.vmdk”
  file_spec.source_type = File.SourceType.PUSH
 
  # 7 - Add the VMDK file spec to the update session.
  file_info = update_file_stub.File.add(update_session_id=session_id, file_spec=file_spec)
  upload_uri = file_info.upload_endpoint().uri
 
  # 8 - Use HTTP library to push the file.
  file_name = “/medias/storage/ubuntu_disk.vmdk”
  host = urlparse.urlsplit(upload_uri)
  connection = httplib.HTTPConnection(host.netloc)
  with open(file_name, “rb”) as f :
    connection.request(“PUT”, upload_uri, f)
 
  # 9 - Commit the updates.
  library_item_service.UpdateSession.complete(session_id)
 
finally :
  # 10 - Delete the session.
  library_item_service.UpdateSession.delete(session_id)