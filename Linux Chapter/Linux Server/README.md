# Linux_Server
BeCode Linux Server-Client Project

## Table of Contents
- [Project task](#project-task)
    - [Requirements](#requirements)

- [Server VirtualMachine Setup](#server-virtualmachine-setup)
    - [1. Creating and installing the VM](#1-creating-and-installing-the-vm)
    - [2. Install sudo and add user to sudoers](#2-install-sudo-and-add-user-to-sudoers)
    - [3. Setting up the firewall](#3-setting-up-the-firewall)
    - [4. Setting server's Static IP](#4-setting-servers-static-ip)
    - [5. Installing GLPI](#5-installing-glpi)
    - [6. Setting up a DNS server](#6-setting-up-a-dns-server)
    - [7. Setting up a DHCP server](#7-setting-up-a-dhcp-server)
    - [8. Weekly Backup of Configurations](#8-weekly-backup-of-configurations)
  
- [Workstation VirtualMachine Setup](#workstation-vm-setup)
    - [1. Setting Up the VM](#1-setting-up-the-vm)
    - [2. Installing the consumer Softwares](#2-installing-the-consumer-softwares)

- [_Useful Links_](#useful-links)


---


## Project Task

The local library in your little town has no funding for Windows licenses so the director is considering Linux. Some users are sceptical and ask for a demo. The local IT company where you work is taking up the project and you are in charge of setting up a server and a workstation.
To demonstrate this setup, you will use virtual machines and an internal virtual network (your DHCP must not interfere with the LAN).

You may propose any additional functionality you consider interesting.

## Requirements

Set up the following Linux infrastructure:

1. One server (no GUI) running the following services:
    - DHCP (one scope serving the local internal network)  isc-dhcp-server
    - DNS (resolve internal resources, a redirector is used for external resources) bind
    - HTTP+ mariadb (internal website running GLPI)
    - **Required**
        1. Weekly backup the configuration files for each service into one single compressed archive
        2. The server is remotely manageable (SSH)
    - **Optional**
        1. Backups are placed on a partition located on  separate disk, this partition must be mounted for the backup, then unmounted

2. One workstation running a desktop environment and the following apps:
    - LibreOffice
    - Gimp
    - Mullvad browser
    - **Required** 
        1. This workstation uses automatic addressing
        2. The /home folder is located on a separate partition, same disk 
    - **Optional**
        1. Propose and implement a solution to remotely help a user



-----------------------------------------

# Server VirtualMachine Setup

As our server we'll setup an Ubuntu Server 22.04 virtual machine using VirtualBox.

As required it will be running DHCP, DNS and HTTPS with MariaDB (running on GLPI) services.

*Important note:
before turning on the VM, we will have to change the settings of its Network adaptor. 
Adaptor 1: will be set on Bridge, essential in order to gain internet access directly using the DNS and services of our Host device (Windows).
Adaptor 2: will be set on Host-Only, in this way we will isolate a network between our server and the workstation. Also from our VirtualBox application, we will have to change the options on its Host-only adaptor, setting the DHCP disabled, to verify if the DHCP and DNS services are properly working*

-----------------------------------------

## Steps

### 1. Creating and installing the VM

First we need to download the Ubuntu Server ISO, you can get yours [here](https://ubuntu.com/download/server).

Once the ISO downloaded, we can set up the new VM on VirtualBox.

Click on "NEW", fill out the name, select the ISO you just downloaded and check "Skip Unattended Installation".

Allocate at least 2048MB of RAM and 2 CPU cores since we're gonna run a desktop environment on it.

Allocate 20GB of hard drive space or more.

Finish.

Once the new VM starts running, it will start the configuration process in the terminal:

Select your language.

Select your location.

Choose the host and password of your server.

Don't scan for extra setups as it might slowdown your installation for unnecessary applications, we will install those we need later on.

---

### 2. Install sudo and add user to sudoers

First step, install sudo and add your user to the sudoers group:
```sh
su root
```
```sh
apt install sudo
```
```sh
usermod -aG sudo YOUR_USERNAME
```
```sh
exit
```

Test sudo and privilege:
```sh
sudo apt update
```

-----------------------------------------

### 3. Setting up the firewall

Then we'll install the Uncomplicated Firewall and set it up for the future:
```sh
sudo apt install ufw
```
```sh
sudo ufw enable
```
```sh
sudo ufw allow SSH,80,443,53,67
```

(22 for SSH, 80 for HTTP, 443 for HTTPS, 53 for DNS and 67 for DHCP)

-----------------------------------------

### 4. Setting server's Static IP

After that, we'll be setting a static IP to our server:

```sh
sudo nano /etc/netplan/00-installer-config.yaml
```

Find the lines showed hereunder:
>
>
>

Replace its content with the configuration showed under and with the desired static IP configuration:
```
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s8:
      dhcp4: true
    enp0s3:
       addresses:
        - 192.168.56.101/24
       routes:
        - to: 0.0.0.0/0
          via: 192.168.56.110
       nameservers:
         addresses:
           - 192.168.56.101
           - 8.8.8.8
       dhcp4: no
  version: 2
```
enp0s8 : is the network interface set as bridge in order for us to have internet connection.
It is set to get an IP address directly from the DHCP.

enp0s3 : is set with the desired static IP adddress which in our case will be the Ubuntu Server IP, same as the DHCP and DNS.

You now have a server with a static IP.

-----------------------------------------

### 4. Installing GLPI

We'll use a convenient [little script](https://github.com/jr0w3/GLPI_install_script) that'll install and set up GLPI with and Apache2 server and a MardiaDB database.

We'll have to give it the root privilege:
```sh
su root
```
```sh
wget https://raw.githubusercontent.com/jr0w3/GLPI_install_script/main/glpi-install.sh && bash glpi-install.sh
```

Follow the scripts instructions.

When the script finishes doing its thing, we are supposed to restart apache2 but it wont work, so we run this:
```sh
sudo ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load
```
```sh
sudo systemctl restart apache2
```
```sh
sudo systemctl enable apache2
```
If everything went according to plan, you should be able to access your GLPI interface by going to your machine's IP with a browser. To find the IP, type:
```sh
ip a
```

The default credentials for GLPI are glpi:glpi. (Some other extra credentials will be shown for other users with different permissions)

-----------------------------------------

### 5. Setting up a DNS server

Follow [this tutorial](https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/set-up-dns-server-on-ubuntu-22-04.html).

A few important notes:

* The service is using Bind9 and it utilities in order to work.

* You can use nano instead of vim.

* You will have the option to create an ACL (access list) for trusted Networks to be using the DNS service by adding some more eextra lines on the file "named.conf.options"

```
    acl trustedclients {
            localhost;
            localnets;
            <other network we allow: exp. 172.16.18.0 /24>
        };

then to let acces only to the ACL created :

        recursion yes; 
        allow-query { trustedclients; };     #or any name of the ACL given
        allow-query-cache { trustedclients; };
        allow-recursion { trustedclients; };       

If we want to allow anyone :

        recursion yes; 
        allow-query { any; };
        allow-query-cache { any; };
        allow-recursion { any; };       
```

* Remember to replace the following files and directory's name to your own choice.

-----------------------------------------

### 6. Setting up a DHCP server

First we install it:
```sh
sudo apt install isc-dhcp-server
```
```sh
sudo nano /etc/default/isc-dhcp-server
```

Replace the last 2 lines with:
>INTERFACESv4="enp0s3"  
>#INTERFACESv6=""

Then we configure the DHCP:
```sh
sudo cp /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf.old
```
```sh
sudo nano /etc/dhcp/dhcpd.conf
```

Paste in this config:
```
default-lease-time 600;
max-lease-time 7200;

ddns-update-style none;

authoritative;

option subnet-mask 255.255.0.0;
option broadcast-address [FIRST_THREE_OCTETS_OF_YOUR_NETWORK].255;
option domain-name-servers [YOUR_SERVER_IP];
option domain-name "[YOUR_DOMAIN_NAME]";
option routers [YOUR_ROUTER_IP];

subnet [YOUR_NETWORK] netmask [NETWORK_MASK] {
        range [FROM_IP] [TO_IP];
}
```

For the subnet mask range it is suggested you choose a small range for easier testing, i.e:

```
subnet 192.168.56.0 netmask 255.255.0.0 {
        range 192.168.56.120 10.40.5.150;
}
```
<ins>__Do not include the IP of your own DHCP server, set a range above or below it.__</ins>

Save and restart both VM's.

To verify that it's working proprely, __on your workstation__, run:
```sh
sudo dhclient -v
```

You should see a line like this:
>DHCPOFFER of YOUR_NEW_IP from YOUR_SERVER_IP


The final step to see if your DHCP and DNS are configured proprely and work together is to open a browser, and navigate to YOUR_DOMAIN_NAME that you set up during the DNS configuration. (i.e: I chose "wares.bobby.local" during my DNS config, if you follow the tutorial yours will be "ns1.something.local", that is what you'll navigate to with your browser)

You should be able to access your GLPI interface.

-----------------------------------------

### 7. Weekly Backup of Configurations

First we need to create a new volume for your VM.

1. Shutdown your VM.
2. In VirtualBox, while your VM is selected, go to Settings.
3. Go to storage.
4. Click on the little hard drive on the left of "Controller:SATA".
5. Create on the top left.
6. Leave VDI selected -> Next.
7. Allocate the space you want (at least 5GB).
8. Select your new volume and click on "Choose".

You now have a new volume attached to your VM, to check your available disks on the VM, type:
```sh
lsblk
```

If you see a /dev/sdb then your additional drive exists.

Format the new extra drive to ext4:
```sh
sudo mkfs.ext4 /dev/sdb
```
Create a backup directory in /mnt:
```sh
sudo mkdir /mnt/backups
```

Then we create a cronjob to launch the script every week on Sunday at 00:00.

```sh
sudo crontab -e
```

Then with nano (or any text editor) create a file with the job to do.
Add the following line at the end of the file:

```
0 0 * * 0 sudo mount /dev/sdb /mnt/backups && sudo cp -R /etc/dhcp/dhcpd.conf /mnt/backups/dhcpd.conf.backup && sudo cp /etc/bind/named.conf /mnt/backups/named.conf.backup && sudo cp -R /etc/bind/named.conf.local /mnt/backups/zones && sudo cp -R /etc/apache2 /mnt/backups/apache2 && sudo cp -R /etc/mysql/mariadb.conf.d /mnt/backups/mariadb.conf.d.backup && sudo cp -R /var/www/html/glpi /mnt/backups/glpi && cd /mnt/backups && sudo tar -czvf backups.tar.gz * && sudo umount /mnt/backups
```

-----------------------------------------


# Workstation VM Setup

We'll setup a Kali Linux virtual machine with a graphical desktop environment using VirtualBox.

*Important note:
before turning on the VM, we will have to change the settings of its Network adaptor. 
Adaptor 1: will be set on Bridge, essential in order to gain internet access directly using the DNS and services of our Host device (Windows).
Adaptor 2: will be set on Host-Only, in this way we will isolate a network between our server and the workstation. Also from our VirtualBox application, we will have to change the options on its Host-only adaptor, setting the DHCP disabled, to verify if the DHCP and DNS services are properly working.*

## Step

-----------------------------------------

### 1. Setting Up the VM

Once your machine is turned on, the first thing we have to do is add your user to the sudoers.

```sh
su root
```
```sh
sudo usermod -aG sudo YOUR_USERNAME
```
```sh
exit
```
Restart your VM

-----------------------------------------


### 2. Installing the consumer Softwares

[Libre Office](https://www.libreoffice.org/)
LibreOffice is installed by default on most popular linux distributions, but if it isn't on yours, type
```sh
sudo apt install libreoffice
```

[GIMP](https://www.gimp.org/)
```sh
sudo apt install gimp
```

[MULLVAD Browser](https://mullvad.net/en/download/browser/linux)

Download it from their website.

```sh
cd Downloads
```
```sh
tar xf mullvad-browser-linux64-[YOUR_VERSION].tar.xf
```
```shpo
rm mullvad-browser-linux64-[YOUR_VERSION].tar.xf
```
```sh
mv mullvad-browser ~/
```
```sh
cd
```
```sh
cd mullvad-browser
```
```sh
./start-mullvad-browser-desktop --register-app
```

Now you have Mullvad browser registered in your applications.


-----------------------------------------

## Useful Links

**Remote help** :
If we want to set up the option of a remote help, we can use a Windows default application Remote Desktop Protocol or a Third-party remote Desktop Software.

*To keep in mind that the RDP (Remote Desktop Protocol) service is provided only to Windows 10 or 11 with Pro edition, the Home Edition does not support the default Remote Desktop Protocol*

For a Step-by-step [follow this Tutorial.](https://www.makeuseof.com/tag/how-to-establish-simple-remote-desktop-access-between-ubuntu-and-windows/)

---


[CHAT-GPT](https://openai.com/blog/chatgpt) - For any kind of troubleshooting! 

[crontab.guru](https://crontab.guru/) to help you understand and configure a cronjob.

[Nmap](https://nmap.org/) to easily check what ports are open on your machine.
```sh
sudo apt install nmap
```
```sh
nmap localhost
```
