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

# create an SFTP client object
ftp = ssh_client.open_sftp()

# download a file from the remote server
files = ftp.put(r'F:\Data Engineering\ftplib\download_folder','/ftp/upload')

# close the connection
ftp.close()
ssh_client.close()