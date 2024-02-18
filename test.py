# Import FTP from ftplib
import ftplib

# Connection parameters
ftpHost = 'localhost'
ftpPort = 21
ftpUsername = 'test'
ftpPassword = 'test'

# Connect FTP Server
ftp_server = ftplib.FTP(ftpHost, ftpUsername, ftpPassword)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"
 
# Send quit
ftp_server.quit()

print("FTP Connection Complete...")