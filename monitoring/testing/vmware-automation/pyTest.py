OS = [ubuntu, centos, windows10, ESXi6]

@pytest.mark.paramaterized('operating_system', OS.keys())
def test_operating_systems_boot(setup, operating_system):
	guest = OS[operating_system]()
	setup.add_guest_to_setup(guest)
	setup.run()
	verufi_guest_booted(setup)