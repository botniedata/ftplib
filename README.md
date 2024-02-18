### 02172024

- adds file README.md
- adds requirements.txt
    -ftplib
    -pandas
    -sqlalchemy
    -requests
    -psycopg2
- del ftplib from requirements.txt
- pip install -r requirements.txt
- ftp connection verified

### Check WSL List
|   code                                |   description                                 |
|---------------------------------------|-----------------------------------------------|
|   `wsl -l`                            |   to see a list of installed distro names     |
|   `wsl --unregister <Distri Name>`    |   to remove installed wsl distri              |   
|   `wsl --install -d <Distri Name>`    |   to install wsl distri                       |

### Install an FTP Server via Ubuntu with VSFTPD
|   code                                |   description                                 |
|---------------------------------------|-----------------------------------------------|
|   `sudo apt update`                   |   to check updates to Ubuntu                  |
|   `sudo apt upgrade`                  |   to install upgrades to Ubuntu               |
|   `sudo apt install vsftpd`           |   to install FTP Server                       |
|   `sudo service vsftpd status`        |   to check status of FTP Server               |

### To check if the FTP Server is running
|   Note                                |   description                                     |
|---------------------------------------|---------------------------------------------------|
|   `Active: active (running)`          |   if you see this command the FTP is `running`    |

### To Stop and Start Services of FTP Server
|   Note                                |   description                                     |
|---------------------------------------|---------------------------------------------------|
|   `sudo service vsftpd start`         |   to start FTP Server Services                    |
|   `sudo service vsftpd stop`          |   to stop FTP Server Services                     |

### Configure the FTP Server
|   file                                |   code                                                        |   description                                                                         |
|---------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------|
|   `/etc/vsftpd.config`                |    `sudo cp /etc/vsftpd.config /etc/vsftpd.config_backdate`   |   to create a back-up file before configuration                                       |
|   `/etc/vsftpd.config`                |    remove the # from `local_enable=YES`                       |   to allow local users to log in                                                      | 
|   `/etc/vsftpd.config`                |    remove the # from `write_enable=YES`                       |   to enable any form of FTP write command (upload)                                    |
|   `/etc/vsftpd.config`                |    remove the # from `chroot_local_user=YES`                  |   to restrict local user to HOME directories                                          |
|   `/etc/vsftpd.config`                |    go to the bottom file add `user_sub_token=$USER`           |   to redirect the user routes to `/home/$USER/ftp`                                    |
|   `/etc/vsftpd.config`                |    go to the bottom file add `local_root=/home/$USER/ftp`     |   to redirect the user routes to `/home/$USER/ftp`                                    |
|   `/etc/vsftpd.config`                |    go to the bottom file add `pasv_min)port=10000`            |   to resolve if there's any firewall issue between server and client (port 20, 21)    |
|   `/etc/vsftpd.config`                |    go to the bottom file add `pasv_min)port=10100`            |   to resolve if there's any firewall issue between server and client (port 20, 21)    |

### To save /etc/vsftpd/ file
|   Note                                |   description                                     |
|---------------------------------------|---------------------------------------------------|
|   press `CTRL + O` then ENTER         |   to save modification                            |
|   press `CTRL + X` then ENTER         |   to exit editing mode                            |