import ftplib

# connection parameter
ftpHost = 'localhost'
ftpUName = 'depph'
ftpPWord = 'depph'
ftpPort = 21

# ftp client instance
ftp = ftplib.FTP_TLS(timeout=30)

# connect to the FTP server
ftp.connect(ftpHost, ftpPort)

# login to the FTP server
ftp.login(ftpUName, ftpPWord)

# setup secure data connection
ftp.prot_p()

# some

#
ftp.quit()

print("FTP Connection Complete!")