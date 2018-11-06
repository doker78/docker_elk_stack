...
 
# Specify the resource to be captured.
deployable_identity = ovf_client.LibraryItem.DeployableIdentity();
deployable_identity.type = “VirtualMachine”
deployable_identity.id = “vm-32”
 
# Create a target spec to identify a library to hold the new item.
create_target = ovf_client.LibraryItem.CreateTarget()
create_target.library_id = my_library_id
 
# Specify OVF properties.
create_spec = ovf_client.LibraryItem.CreateSpec()
create_spec.name = “snap-32”
create_spec.description = “Snapshot of VM-32”
 
# Initiate synchronous capture operation.
lib_item_stub = ovf_client.LibraryItem(my_stub_config)
client_token = str(uuid.uuid4())
result = lib_item_stub.create(source=deployable_identity,
                              target=create_target,
                              create_spec=create_spec,
                              client_token=client_token)
 
# Verify capture status.
print("Resource Type={} (ID={}) status:".format(deployable_identity.type, deployable_identity.id))
 
if result.succeeded == True :
  print("Resource captured.")
else :
  print("Capture failed.")
if result.error is not None :
  for error in result.error.errors :
    print("Error {}".format(error.message))
  if len(result.error.warnings) > 0 :
    print("Warnings:")
    for warning in result.error.warnings :
      print("{}".format(warning.message))
  if len(result.error.information) > 0 :
    print("Messages:")
    for info in result.error.information :
      for message in info.messages :
        print("{}".format(message))