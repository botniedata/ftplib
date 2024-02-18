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


|   Note                                |   description                                     |
|---------------------------------------|---------------------------------------------------|
|   `Active: active (running)`          |   if you see this command the FTP is `running`    |

### Configure the FTP Server
|   settings                            |   description                                 |
|---------------------------------------|-----------------------------------------------|
|   `sudo apt update`                   |   to check updates to Ubuntu                  |