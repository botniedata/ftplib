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

# display files and directories
files = ftp.listdir()
print(f"Listing all the files and Directory: {files}\n")

# download a file from the remote server
local_file_path = r'F:\Data Engineering\ftplib\download_folder\sample.txt'
remote_file_path = '/ftp/upload/'

# download a file from the remote server
files = ftp.put(local_file_path, remote_file_path)

ftp.close()
ssh_client.close()