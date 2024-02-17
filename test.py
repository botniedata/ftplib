# Import FTP from ftplib
from ftplib import FTP_TLS

# Connection parameters
ftpHost = 'localhost'
ftpPort = 21
ftpUsername = 'test'
ftpPassword = 'admin'

# FTP timeout
ftp = FTP_TLS(timeout=30)

# Connect to the FTP server
ftp.connect(ftpHost, ftpPort)

# Login credentials
ftp.login(ftpUsername, ftpPassword)

# download files from FTP Server
ftp.cwd("/Data Engineering")

# Setup secure connection
ftp.prot_p()

# -->

# Send quit
ftp.quit()

print("FTP Login Complete...")