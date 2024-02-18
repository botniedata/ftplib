# Import FTP from ftplib
from ftplib import FTP_TLS

# Connection parameters
ftpHost = 'localhost'
ftpPort = 21
ftpUsername = 'depph'
ftpPassword = 'depph'

# FTP timeout
ftp = FTP_TLS(timeout=30)

# Connect to the FTP server
ftp.connect(ftpHost, ftpPort)

# Login credentials
ftp.login(ftpUsername, ftpPassword) 

# Send quit
ftp.quit()

print("FTP Connection Complete...")