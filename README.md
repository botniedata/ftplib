## Windows Subsystem for Linux (WSL) with VSFTPD Server

### Table of Content

|   No  |   Name                                                                                                              |
|:-----:|---------------------------------------------------------------------------------------------------------------------|
|   1   |   [Check and Install Distro WSL](#check-wsl-list-and-install-distro)                                                |
|   2   |   [Update, Upgrade, Install and Check the FTP Server Status](#install-an-ftp-server-via-ubuntu-with-vsftpd)         |
|   3   |   [Check the FTP Service is Running](#check-the-ftp-service-is-running)                                             |
|   4   |   [Stop and Start FTP Service](#stop-and-start-ftp-service)                                                         |
|   5   |   [Configure /etc/vsftpd.conf file](#configure-the-ftp-server)                                                      |
|   6   |   [Save configured /etc/vsftpd.conf file](#save-etcvsftpd-file)                                                     |
|   7   |   [Restarts configured /etc/vsftpd.conf file](#restart-system-services-after-modify-etcvsftpdconfig)                |
|   8   |   [Enable Ports and Passive Firewall](#enable-ports-and-passive-firewall)                                           |
|   9   |   [Creates New User](#creates-new-user)                                                                             |
|  10   |   [Make Directory for New User](#make-directory-for-new-user)                                                       |
|  11   |   [Make Ownership for New User](#make-ownership-for-new-user)                                                       |
|  12   |   [Remove Root Access for New User](#remove-root-access-for-new-user)                                               |
|  13   |   [Create Upload Folder](#create-upload-folder)                                                                     |
|  14   |   [Create Ownership User to Upload Folder](#create-ownership-user-to-upload-folder)                                 |
|  15   |   [Create a sample text file](#create-a-sample-text-file)                                                           |
|  16   |   [Check User's Permission](#check-users-permission)                                                                |
|  17   |   [Adds New User to vsftpd.userlist](#adds-new-user-to-vsftpduserlist)                                              |
|  18   |   [Secure Connection via OPENSSL](#secure-connection-via-openssl)                                                   |
|  19   |   [Add SSL Private Key to /etc/vsftpd.conf file](#add-ssl-private-key-to-etcvsftpdconf-file)                        |
|  EOD  |   [End of Document](#end-of-document)                                                                               |

### Check WSL List and Install Distro
|   code                                |   description (PowerShell)                    |
|---------------------------------------|-----------------------------------------------|
|   `wsl -l`                            |   to see a list of installed distro names     |
|   `wsl --unregister <Distri Name>`    |   to remove installed wsl distri              |   
|   `wsl --install -d <Distri Name>`    |   to install wsl distri                       |

### Install an FTP Server via Ubuntu with VSFTPD
|   code                                |   description (WSL Ubuntu)                    |
|---------------------------------------|-----------------------------------------------|
|   `sudo apt update`                   |   to check updates to Ubuntu                  |
|   `sudo apt upgrade`                  |   to install upgrades to Ubuntu               |
|   `sudo apt install vsftpd`           |   to install FTP Server                       |
|   `sudo service vsftpd status`        |   to check status of FTP Server               |

### Check the FTP Service is Running
|   Note                                |   description (WSL Ubuntu)                        |
|---------------------------------------|---------------------------------------------------|
|   `Active: active (running)`          |   if you see this command the FTP is `running`    |

### Stop and Start FTP Service
|   Note                                |   description (WSL Ubuntu)                        |
|---------------------------------------|---------------------------------------------------|
|   `sudo service vsftpd start`         |   to start FTP Server Services                    |
|   `sudo service vsftpd stop`          |   to stop FTP Server Services                     |


### Configure the FTP Server
|   file                                |   code                                                           |   description (WSL Ubuntu)                                                            |
|---------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------|
|   `/etc/vsftpd.config`                |    `sudo cp /etc/vsftpd.conf /etc/vsftpd.conf_orig`              |   to create a back-up file before configuration                                       |
|   sudo nano `/etc/vsftpd.config`      |    remove the # from `local_enable=YES`                          |   to allow local users to log in                                                      | 
|   sudo nano `/etc/vsftpd.config`      |    remove the # from `write_enable=YES`                          |   to enable any form of FTP write command (upload)                                    |
|   sudo nano `/etc/vsftpd.config`      |    remove the # from `chroot_local_user=YES`                     |   to restrict local user to HOME directories                                          |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `user_sub_token=$USER`              |   to redirect the user routes to `/home/$USER/ftp`                                    |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `local_root=/home/$USER/ftp`        |   to redirect the user routes to `/home/$USER/ftp`                                    |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `pasv_min_port=10000`               |   to resolve if there's any firewall issue between server and client (port 20, 21)    |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `pasv_min_port=10100`               |   to resolve if there's any firewall issue between server and client (port 20, 21)    |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `userlist_file=/etc/vsftpd.userlist`|   to allow only users on the userlist to access                                       |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `userlist_deny=NO`                  |   to allow only users on the userlist to access                                       |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `allow_anon_ssl=NO`                 |   to restrict anonymous access                                                        |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `force_local_data_ssl=YES`          |   to restrict anonymous access                                                        |
|   sudo nano `/etc/vsftpd.config`      |    go to the bottom file add `force_local_logins_ssl_YES`        |   to restrict anonymous access                                                        |

### Save /etc/vsftpd/ file
|   Note                                |   description (WSL Ubuntu)                        |
|---------------------------------------|---------------------------------------------------|
|   press `CTRL + O` then ENTER         |   to save modification                            |
|   press `CTRL + X` then ENTER         |   to exit editing mode                            |

### Restart System Services after modify /etc/vsftpd.config
|   Note                                |   description (WSL Ubuntu)                        |
|---------------------------------------|---------------------------------------------------|
|   `sudo systemctl restart vsftpd`     |   to restart FTP Server Services                  |

### Enable Ports and Passive Firewall
|   code                                                                |   description (WSL Ubuntu)                                          |
|-----------------------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo ufw allow from any to any port 20,21,10000:10100 proto tcp`   |   to enable ports 20 and 21, firewall 10000 and 101000 from /etc/   |
|   [sudo] password for admin:                                          |   Rules updated... Rules updated (v6)                               |

### Creates New User
|   code                    |   description (WSL Ubuntu)                                          |
|---------------------------|---------------------------------------------------------------------|
|   `sudo adduser phil`     |   to create a new user ... adds user details                        |

### Make Directory for New User
|   code                            |   description (WSL Ubuntu)                                          |
|-----------------------------------|---------------------------------------------------------------------|
|   `sudo mkdir /home/phil/ftp`     |   to create home directory ftp for the user                         |

### Make Ownership for New User
|   code                                                |   description (WSL Ubuntu)                                          |
|-------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo chown nobody:nogroup /home/<user>/ftp`        |   to create ownership to the created user                           |

### Remove Root Access for New User
|   code                                                |   description (WSL Ubuntu)                                          |
|-------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo chmod a-w /home/<user>/ftp`                   |   to remove root access to the created user                         |

### Create Upload Folder
|   code                                                |   description (WSL Ubuntu)                                          |
|-------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo mkdir /home/<user>/ftp/upload`                |   to create upload folder                                           |

### Create Ownership User to Upload Folder
|   code                                                |   description (WSL Ubuntu)                                          |
|-------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo chown <user>:<user> /home/phil/ftp/upload`    |   to create ownership to the ftp user upload                        |

### Create a sample text file
|   code                                                                                  |   description (WSL Ubuntu)                                          |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|   ```echo "<some-message>" (pipe) sudo tee /home/<user>/ftp/upload/sample.txt```        |   to create a simple file from upload folder                        |

### Check User's Permission
|   code                                                                                  |   description (WSL Ubuntu)                                          |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo ls -la /home/<user>/ftp`                                                        |   to check permission of created user                               |

### Adds New User to vsftpd.userlist
|   code                                                                                  |   description (WSL Ubuntu)                                          |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|   `echo "<user>" (pipe) sudo tee -a /etc/vsftpd.userlist`                               |   to add create user to allow to access FTP Server                  |


### Secure Connection via OPENSSL
|   code (WSL Ubuntu)                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   `sudo openssl req -x509 -nodes -days 3650 -newkey  rsa:2048 -keyout /etc/ssl/private/vsftpd.pem -out /etc/ssl/private/vsftpd.pem`                           |

|   Description                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   it will generate 2048-bit private key and self-signed SSL Certificate... and to enter information will be incorporated to the certificate request           |

### Add SSL Private Key to /etc/vsftpd.conf file
|   code (WSL Ubuntu)                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   `rsa_cert_file=/etc/ssl/private/vsftpd.pem`                                                                                                                 |
|   `rsa_private_file=/etc/ssl/private/vsftpd.pem`                                                                                                              |
|   `ssl_enable=YES`                                                                                                                                            |

|   code                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   it will generate 2048-bit private key and self-signed SSL Certificate... and to enter information will be incorporated to the certificate request           |

### End of Document 
[Table of Contents](#table-of-content)