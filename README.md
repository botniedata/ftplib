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
|   file                                |   code                                                           |   description                                                                         |
|---------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------|
|   `/etc/vsftpd.config`                |    `sudo cp /etc/vsftpd.config /etc/vsftpd.config_backdate`      |   to create a back-up file before configuration                                       |
|   `/etc/vsftpd.config`                |    remove the # from `local_enable=YES`                          |   to allow local users to log in                                                      | 
|   `/etc/vsftpd.config`                |    remove the # from `write_enable=YES`                          |   to enable any form of FTP write command (upload)                                    |
|   `/etc/vsftpd.config`                |    remove the # from `chroot_local_user=YES`                     |   to restrict local user to HOME directories                                          |
|   `/etc/vsftpd.config`                |    go to the bottom file add `user_sub_token=$USER`              |   to redirect the user routes to `/home/$USER/ftp`                                    |
|   `/etc/vsftpd.config`                |    go to the bottom file add `local_root=/home/$USER/ftp`        |   to redirect the user routes to `/home/$USER/ftp`                                    |
|   `/etc/vsftpd.config`                |    go to the bottom file add `pasv_min)port=10000`               |   to resolve if there's any firewall issue between server and client (port 20, 21)    |
|   `/etc/vsftpd.config`                |    go to the bottom file add `pasv_min)port=10100`               |   to resolve if there's any firewall issue between server and client (port 20, 21)    |
|   `/etc/vsftpd.config`                |    go to the bottom file add `userlist_file=/etc/vsftpd.userlist`|   to allow only users on the userlist to access                                       |
|   `/etc/vsftpd.config`                |    go to the bottom file add `userlist_deny=NO`                  |   to allow only users on the userlist to access                                       |
|   `/etc/vsftpd.config`                |    go to the bottom file add `allow_anon_ssl=NO`                 |   to restrict anonymous access                                                        |
|   `/etc/vsftpd.config`                |    go to the bottom file add `force_local_data_ssl=YES`          |   to restrict anonymous access                                                        |
|   `/etc/vsftpd.config`                |    go to the bottom file add `force_local_logins_ssl_YES`        |   to restrict anonymous access                                                        |

### To save /etc/vsftpd/ file
|   Note                                |   description                                     |
|---------------------------------------|---------------------------------------------------|
|   press `CTRL + O` then ENTER         |   to save modification                            |
|   press `CTRL + X` then ENTER         |   to exit editing mode                            |

### To Restart system services after modify /etc/vsftpd.config
|   Note                                |   description                                     |
|---------------------------------------|---------------------------------------------------|
|   `sudo systemctl restart vsftpd      |   to restart FTP Server Services                  |

### Allow configured ports and passive firewall
|   code                                                                |   description                                                       |
|-----------------------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo ufw allow from any to any port 20,21,10000:101000 proto tcp`  |   to enable ports 20 and 21, firewall 10000 and 101000 from /etc/   |
|   [sudo] password for admin:                                          |   Rules updated... Rules updated (v6)                               |

### Adds User access FTP
|   code                    |   description                                                       |
|---------------------------|---------------------------------------------------------------------|
|   `sudo adduser phil`     |   to create a new user ... adds user details                        |

### Make a directory for the user
|   code                            |   description                                                       |
|-----------------------------------|---------------------------------------------------------------------|
|   `sudo mkdir /home/phil/ftp`     |   to create home directory ftp for the user                         |

### Create ownership for the user
|   code                                                |   description                                                       |
|-------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo chown nobody:nogroup /home/<user>/ftp`        |   to create ownership to the created user                           |

### Remove root access commnand for the user
|   code                                                |   description                                                       |
|-------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo chmod a-w /home/<user>/ftp`                   |   to remove root access to the created user                         |

### Create upload directory
|   code                                                |   description                                                       |
|-------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo mkdir a-w /home/<user>/ftp/upload`            |   to create upload folder                                           |

### Create ownershiop upload
|   code                                                |   description                                                       |
|-------------------------------------------------------|---------------------------------------------------------------------|
|   `sudo chown <user>:<user> /home/phil/ftp/upload`    |   to create ownership to the ftp user upload                        |

### Create a sample file to upload
|   code                                                                                  |   description                                                       |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|   ```echo "My FTP Server Message (pipe) sudo tee /home/phil/ftp/upload/sample.txt```    |   to create a simple file from upload folder                        |

### Secure Connection via openssl
|   code                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   `sudo openssl req -x509 -nodes - days 3650 -newkey  rsa:2048 -keyout /etc/ssl/private/vsftpd.pem -out /etc/ssl/private/vsftpd.pem`                          |

|   Description                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   it will generate 2048-bit private key and self-signed SSL Certificate... and to enter information will be incorporated to the certificate request           |

### Add SSL Private Key
|   code                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   `rsa_cert_file=/etc/ssl/private/vsftpd.pem`                                                                                                                 |
|   `rsa_private_file=/etc/ssl/private/vsftpd.pem`                                                                                                              |
|   `ssl_enable=YES`                                                                                                                                            |

|   code                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   it will generate 2048-bit private key and self-signed SSL Certificate... and to enter information will be incorporated to the certificate request           |
