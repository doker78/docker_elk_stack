...
 
# Create a VM deployment specification to accept any network resource.
deployment_spec = ovf_client.LibraryItem.ResourcePoolDeploymentSpec()
deployment_spec.accept_all_eula = True
 
# Create deployment target spec to accept any resource pool.
target_spec = ovf_client.LibraryItem.DeploymentTarget()
 
# Initiate synchronous deployment operation.
item_stub = ovf_client.LibraryItem(my_stub_config)
result = item_stub.deploy(my_library_item_id,
                          target_spec,
                          deployment_spec,
                          client_token=str(uuid.uuid4())
 
# Verify deployment status.
print("Resource Type={} (ID={}) status:".format(result.resource_id.type, result.resource_id.id))
if result.succeeded == True :
  print("Resource instantiated.")
else :
  print("Instantiation failed.")
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