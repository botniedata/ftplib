import paramiko

# create ssh client 
ssh_client = paramiko.SSHClient()

# remote server credentials
host = "localhost"
username = "depph"
password = "depph"
port = 22

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

ftp = ssh_client.open_sftp()
files = ftp.listdir()

print("Listing all the files and Directory: ",files)

# close the connection
ftp.close()
ssh_client.close()