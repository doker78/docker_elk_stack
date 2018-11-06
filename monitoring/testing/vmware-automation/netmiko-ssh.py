from netmiko import ConnectHandler

network_device = {
	'device_type': 'cisco_ios',
	'ip': '1.1.1.2'
	'username':'cisco',
	'password': 'cisco'
}

ssh_connection = ConnectHandler(**network_device)

## sending commands to network devices

output = ssh_connection.send_command('sh ip int br')

ssh_connection.disconnect()

print(output)

## sendiong configuration commands

config_commands = [
"interface FastEthernet 1/0"
"ip address 50.50.50.50 255.255.255.0"
]

output = ssh_connection.send_config_set(config_commands)

ssh_connection.disconnect()

print(output)