   vm = None
   vm_name = None
   stub_config = None

   server, username, password, cleardata, skip_verification, vm_name = \
            parse_cli_args_vm(testbed.config['VM_NAME_DEFAULT'])
    stub_config = vapiconnect.connect(server, username, password, skip_verification)
    
    # Get the virtual machine ID
    vm = get_vm(stub_config, vm_name)

    # Create the Power stub  for running power operations on virtual machines 
    vm_power_svc = Power(stub_config)
    vm_power_svc.start(vm)