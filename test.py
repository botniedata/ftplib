# Import FTP from ftplib
from ftplib import FTP_TLS

# Connection parameters
ftpHost = 'localhost'
ftpPort = 21
ftpUsername = 'test'
ftpPassword = 'test'

# FTP timeout
ftp = FTP_TLS(timeout=30)

# Connect to the FTP server
ftp.connect(ftpHost, ftpPort)

# Login credentials
ftp.login(ftpUsername, ftpPassword) 

# Change Directory
ftp.cwd("/")

# Send quit
ftp.quit()

print("FTP Connection Complete...")