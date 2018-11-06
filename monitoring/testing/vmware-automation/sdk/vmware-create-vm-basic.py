...

def create_basic_vm(stub_config, placement_spec, standard_network):
    """
    Create a basic VM.

    Using the provided PlacementSpec, create a VM with a selected Guest OS
    and provided name.

    Create a VM with the following configuration:
    * Create 2 disks and specify one of them on scsi0:0 since it's the boot disk
    * Specify 1 ethernet adapter using a Standard Portgroup backing
    * Setup for PXE install by selecting network as first boot device

    Use guest and system provided defaults for most configuration settings.
    """
    guest_os = testbed.config['VM_GUESTOS']

    boot_disk = Disk.CreateSpec(type=Disk.HostBusAdapterType.SCSI,
                                scsi=ScsiAddressSpec(bus=0, unit=0),
                                new_vmdk=Disk.VmdkCreateSpec())
    data_disk = Disk.CreateSpec(new_vmdk=Disk.VmdkCreateSpec())

    nic = Ethernet.CreateSpec(
        start_connected=True,
        backing=Ethernet.BackingSpec(
            type=Ethernet.BackingType.STANDARD_PORTGROUP,
            network=standard_network))
 
    boot_device_order = [BootDevice.EntryCreateSpec(BootDevice.Type.ETHERNET),
                         BootDevice.EntryCreateSpec(BootDevice.Type.DISK)]

    vm_create_spec = VM.CreateSpec(name=vm_name,
                                   guest_os=guest_os,
                                   placement=placement_spec,
                                   disks=[boot_disk, data_disk],
                                   nics=[nic],
                                   boot_devices=boot_device_order)
    print('\n# Example: create_basic_vm: Creating a VM using spec\n-----')
    print(pp(vm_create_spec))
    print('-----')

    vm_svc = VM(stub_config)
    vm = vm_svc.create(vm_create_spec)

    print("create_basic_vm: Created VM '{}' ({})".format(vm_name, vm))

    vm_info = vm_svc.get(vm)
    print('vm.get({}) -> {}'.format(vm, pp(vm_info)))

    return vm