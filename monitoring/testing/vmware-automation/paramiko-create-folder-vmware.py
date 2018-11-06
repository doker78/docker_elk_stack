import paramiko
ssh_connection = paramiko.SSHClient()

### clonning VM with paramiko 
ssh_connection.set_missing_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect("1.1.1.50", username='username', password='password')

stdin, stdout, stderr = ssh_connection.exec_command("mkdir /vmfs/volumes/datastore1/<vmanme>")
