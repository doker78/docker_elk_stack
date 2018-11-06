from pyVmomi import vim 
from pyVim.connect import SmartConnect


api_connection = SmartConnect(host='1.1.1.50',
	user='username'
	pwd='password'
	port=443,
	sslContext=context)
if not api_connection : 
	print("Cannot connect to a psecified host using specified credentials\n")
	sys.exit()

## create port group
content = api_connection.RetrieveContent()
host_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True)
hostsObjects = [host for host in host_view.view]
host_view.Destroy()

for hosts in hostsObject:
	portgroup_spec = vim.host.PortGroup.Specification()
	portgroup_spec.vswitchName = "<vswitch_name>"
	portgroup_spec.name = "<portgroup_name>"
	portgroup_spec.vlanid = <vlanid>
	host.configManager.networkSystem.AddPortGroup(portgroup_spec)
