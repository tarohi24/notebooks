#!/usr/bin/env bash

if [ `whoami` != "root" ]; then
    echo "This script requires root permission."
    exit 1
fi

read -p "Enter username: "  USR
sudo adduser --gecos '' ${USR}

# .ssh
cd /home/${USR}
mkdir .ssh
cd .ssh
echo "Publickey: "
read PBK
echo $PBK > authorized_keys
cd ..
chown -R ${USR}:${USR} .ssh

# Add to docker member
usermod -aG docker ${USR}
