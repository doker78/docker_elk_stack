import paramiko
ssh_connection = paramiko.SSHClient()

### clonning VM with paramiko 
ssh_connection.set_missing_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect("1.1.1.50", username='username', password='password')

stdin, stdout, stderr = ssh_connection.exec_command("mkdir /vmfs/volumes/datastore1/<vmanme>")

# copy vmx file to esxi via sftp

localpath='<vmname>.vmx'

remotepath='/vmfs/volumes/datastore1/<dir>/<vmname>.vmx'

sftp = ssh_connection.open_sftp()

sftp.put(localpath, remotepath)

sftp.close()

## copy vmdk 

source="/vmfs/volumes/datasrstore1/<sourcevm>/sourcevm_0.vmdk"

destination="/vmfs/volumes/datasrstore1/<vmname>/<<VM NAME>>_0.vmdk"

stdin, stdout, stderr =
ssh_connection.exec_command("vmkfstools -i" + source + "" + destination)

## register and power on a vm

stdin, stdout, stderr = 
ssh_connection.exec_command("vim-cmd vmsvc/pwer.on<vmid>")

