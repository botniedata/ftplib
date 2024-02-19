import ftplib

def getFtpFilenames(ftpHost, ftpPort, ftpUname, ftpPass, remoteWorkingDirectory):
    # create an FTP client instance, use the timeout(seconds) parameter for slow connections only
    ftp = ftplib.FTP(timeout=30)
    
    # connect to the FTP server
    ftp.connect(ftpHost, ftpPort)
    
    # login to the FTP server
    ftp.login(ftpUname, ftpPass)

    # change current working directory if specified
    if not (remoteWorkingDirectory == None or remoteWorkingDirectory.strip() == ""):
        _ = ftp.cwd(remoteWorkingDirectory)
    
    # initialize the filenames as an empty list
    fnames = []
    
    try:
        # use nlst function to get the list of filenames
        fnames = ftp.nlst()
    except ftplib.error_perm as resp:
        if str(resp) == "550 No files found":
            fnames = []
        else:
            raise
    
    # send QUIT command to the FTP server and close the connection
    ftp.quit()

    # return the list of filenames
    return fnames

# connection parameters
ftpHost = 'localhost'
ftpPort = 22
ftpUname = 'depph'
ftpPass = 'depph'
fnames = getFtpFilenames(ftpHost, ftpPort, ftpUname, ftpPass, "/ftp/upload")
print(fnames)
print("execution complete...")