...

vm = None
vm_name = None
stub_config = None
ethernet_svc = None
cleardata = False
nics_to_delete = []
orig_nic_summaries = None
...

        server, username, password, cleardata, skip_verification, vm_name = \
            parse_cli_args_vm(testbed.config['VM_NAME_DEFAULT'])
        stub_config = vapiconnect.connect(server,
                                          username,
                                          password,
                                          skip_verification)

    global vm
    vm = get_vm(stub_config, vm_name)
    if not vm:
        exit('Sample requires an existing vm with name ({}). '
             'Please create the vm first.'.format(vm_name))
    print("Using VM '{}' ({}) for Disk Sample".format(vm_name, vm))

    # Get standard portgroup to use as backing for sample
    standard_network = network_helper.get_standard_network_backing(
        stub_config,
        testbed.config['STDPORTGROUP_NAME'],
        testbed.config['VM_DATACENTER_NAME'])

    # Create Ethernet stub used for making requests
    global ethernet_svc
    ethernet_svc = Ethernet(stub_config)
    vm_power_svc = Power(stub_config)
    nic_summaries = ethernet_svc.list(vm=vm)

    # Save current list of Ethernet adapters to verify that we have cleaned
    # up properly
    global orig_nic_summaries
    orig_nic_summaries = nic_summaries

    global nics_to_delete

    # Create Ethernet Nic using STANDARD_PORTGROUP with the default settings
    nic_create_spec = Ethernet.CreateSpec(
        backing=Ethernet.BackingSpec(
            type=Ethernet.BackingType.STANDARD_PORTGROUP,
            network=standard_network))
    nic = ethernet_svc.create(vm, nic_create_spec)
    nics_to_delete.append(nic)
    nic_info = ethernet_svc.get(vm, nic)

    # Create Ethernet Nic by using STANDARD_PORTGROUP 
    nic_create_spec = Ethernet.CreateSpec(
        start_connected=True,
        allow_guest_control=True,
        mac_type=Ethernet.MacAddressType.MANUAL,
        mac_address='01:23:45:67:89:10',
        wake_on_lan_enabled=True,
        backing=Ethernet.BackingSpec(
            type=Ethernet.BackingType.STANDARD_PORTGROUP,
            network=standard_network))
    nic = ethernet_svc.create(vm, nic_create_spec)
    nics_to_delete.append(nic)
    nic_info = ethernet_svc.get(vm, nic)

    # Update the Ethernet NIC with a different backing
    nic_update_spec = Ethernet.UpdateSpec(
        backing=Ethernet.BackingSpec(
            type=Ethernet.BackingType.STANDARD_PORTGROUP,
            network=standard_network))
    ethernet_svc.update(vm, nic, nic_update_spec)
    nic_info = ethernet_svc.get(vm, nic)
    
    # Update the Ethernet NIC configuration
    nic_update_spec = Ethernet.UpdateSpec(
        wake_on_lan_enabled=False,
        mac_type=Ethernet.MacAddressType.GENERATED,
        start_connected=False,
        allow_guest_control=False)
    ethernet_svc.update(vm, nic, nic_update_spec)
    nic_info = ethernet_svc.get(vm, nic)

    # Powering on the VM to connect the virtual Ethernet adapter to its backing
    vm_power_svc.start(vm)
    nic_info = ethernet_svc.get(vm, nic)

    # Connect the Ethernet NIC after powering on the VM
    ethernet_svc.connect(vm, nic)

    # Disconnect the Ethernet NIC while the VM is powered on
    ethernet_svc.disconnect(vm, nic)