# Theory_&_Questionnaire

## Chapters

### 1. Terminal Basics

#### Pitch

Time to discover the terminal and work with the most common commands.

#### Goals

You should be able to use the right terminal syntax:

- Move around the file system;
- Show the contents of a folder;
- Create a folder
- Create a file
- Change a filename
- Remove a file

As you'll see, the exercises below give you the objective, but not how to do them. When you don't know, it's time to ask your new BFF: Google! That's one core rule at BeCode : before asking your neighbour for help, ask the internet!

### 2. Finding Files

#### Pitch
When you work with linux a graphical user interface is not always available. In most cases, you'll just have the access to a terminal of a remote machine, on which you have just logged in using ssh. It is therefore interesting to be able to use specific commands to easily find a file, folder or even search for pieces of text in files. This is what we will do here.

#### Exercises 
1. Create a file named ``my-file.txt`` with the touch command. Then execute the ``locate my-file.txt`` command. Do you find the file? 
    > Your response : no
1. Run the command sudo ``updatedb``. And run the locate my-file.txt command again. Do you find your file ?
    > Your response : yes
1. With the command ``which``, find the executable file nc and indicate the path
    > Path : /bin/nc
1. With the command ``which``, find the executable file becode. What is the flag ?
    > Command : which becode
    > Flag : BC{WH1CH_FL4G_EXECUTLE_FILE}
1. Search with ``find ``command for a file that contains the name "Edgar Allan Poe". What is the flag ?
    > Command :
    > Flag : BC{3d54r_4ll4n_P03_FL45}
1. Using the ``find`` command, find the file password.txt and specify the flag.
    > Command : find / -name "password.txt" 2>&-
    > Flag : BC{PASSWORD_FILE}
1. With the command ``find``, find a file that starts with ``becode-`` and ends with ``.sh``.
    > Command : find / -name "becode-*" 2>&-
    > Flag : BC{FLAG_FIND_PARTIAL_PATH}
1. Using the ``find`` command to identify any file (not directory) modified in the last day, NOT owned by the root
user and execute ls -l on them. **Chaining/piping commands is NOT allowed!**
    > Your command : find / -type f -mtime -1 -print ! -user root
1. With the find command, find all the files that have an authorization of ``0777``.
    > Your command : find / -type f -perm 0777
1. With the find command, find all the files in the folder ``/home/student/findme/`` that have an authorization of ``0777`` and change the rights of these files to ``0755``
    > Your command : find /home/student/findme/ -type f -perm 0777 -exec chmod 0755 {} \;

### 3. Text Manipulation

#### Pitch
When you work with linux a graphical user interface is not always available. In most cases, you'll just have the access to a terminal of a remote machine, on which you have just logged in using ssh. It is therefore interesting to be able to use specific commands to easily find a file, folder or even search for pieces of text in files. This is what we will do here.

#### Exercices
1. Search all sequences containing "Loxondota" in ``/home/student/lorem.txt``
    > Flag : BC{GREP_ME_LOREM_FL4G}
1. Copy the file /etc/passwd to your home directory. Display the line starting with ``student`` name.
    > Your commands :
    cp /etc/passwd /home/student/
    grep -rn passwd -e "student"
1. Display the lines in the passwd file starting with login names of 3 or 4 characters.
    > Your commands : awk -F: '{if(length($1) == 3 || (length($1) == 4)) print $1}' passwd
1. In the file ``/home/student/sample.txt`` how many different values are there in the first column? in the second?
    > Your response :
    > 
    > Your command :
1. In the file ``/home/student/sample.txt`` sort the values in the second column by frequency of occurrence. (uniq -c can be useful)
    > Your response :
    > Your command :
1. In the file ``/home/student/iris.data`` Change the column separator (comma) to tab (make sure that the changes are applied to the file)
    > Your command : sed 's/,/\t/g' iris.data > iris.data.parsed
1. In the file ``/home/student/iris.data``, extract from this file the column 3 (petal length in cm) (use cut )
    > Your command : cut -f3 d$'\t' iris.data.parsed
1. In the file ``/home/student/iris.data``, count the number of flower species (cut and uniq)
    > Your response : 3
    > Your command : cut -f5 d$'\t' iris.data.parsed | uniq
1. In the file ``/home/student/iris.data``, sort by increasing petal length (see sort options)
    > Your command : sort -k 3 iris.data.parsed
1. In the file ``/home/student/iris.data``, show only lines with petal length greater than the average size
    > Your response :
    > Your command :
1. Using ``/etc/passwd``, extract the user and home directory fields for all users on your student
machine for which the shell is set to ``/bin/false``. 
    > Your response :
    > Your command :

### 4. Piping and Redirection

#### Pitch
Learning the wonders of piping and redirections with the linux terminal

#### Pipe
A pipe is a means of transmitting data from one process to another. It is one of the methods of inter-process communication ("Inter Process Communication": IPC).
A pipe has the following characteristics:
- The communication is unidirectional: we write at one end and read at the other (hence the name tube). This
implies that at least two descriptors are needed to manipulate a tube.
- The communication is done in FIFO (First In First Out) mode, first written, first read. Some primitives
like lseek(), or any other direct access to a data, have no sense for a tube.

What is read leaves the tube permanently and cannot be reread. In the same way, what is written is definitively written
written and cannot be removed.
- The transmission is done in continuous byte flow mode. The consecutive sending of the two sequences "abcd" and
efg" is similar to "abcdefg" and can be read as a whole or in pieces like "ab", "cde" and "fg" for example.
"fg" for example.
- To work, a tube must have at least one reader and one writer. There can be more than one.
- A tube has a finite capacity, and there is a producer/consumer type synchronization between readers and writers: a reader can sometimes and writers: a reader can sometimes wait for something to be written before reading, and a writer can wait for something to be can wait until there is space in the tube before writing.

#### Redirection
Redirects are a way to send data produced by a process to a file or to retrieve
data stored in a file to a process. The standard input, standard output and standard error output
as well as the files from which data is accessed or to which data is sent are all managed by file
by file descriptors. The descriptor duplication mechanism will therefore be the mechanism used to
implement redirections in Unix.

#### Exercices
Read the following [article](https://ryanstutorials.net/linuxtutorial/piping.php) and answer the questions below. Some questions will require additional research.

1. Write the message "hello everyone" in a file called "test" by redirecting the output of the echo command.
    > Your command : echo "hello everyone" > ./test

1. Write the message "goodbye" in the same file "test" by redirecting the output of the echo command and without overwriting the content of "test" and check with the cat command
    > Your command : echo "goodbye" >> ./test

1. Make the ``ls -la`` command redirect to the ``foo`` file
    > Your command : ls -al > foo

1. Execute ``find /etc -name *conf*`` command  and redirect errors (only errors) to a file named err.txt 
    > Your command : find /etc -name *conf* 2> err.txt

1. Repeat the previous exercise, this time redirecting the errors to the linux nothingness.
    > Your command : find /etc -name *conf* 2> /dev/null

1. Now redirect the standard output and the error output of the ``find /etc -name *conf*`` command to two different files (std.out and std.err)
    > Your command :

1. What does the mkfifo command do?
    > No answer required

1. Create a pipe named "MyNammedPipe". Then execute the pwd command which will transmit the data in this pipe. Then use the cat command to read the contents of your "MyNammedPipe" pipe.
    > Your commands :

1. With cat command, add number the lines in the file /etc/passwd with the command ``nl``
    > Your commands :
    
1. Using the previous nl command, the head and tail commands, display the lines of /etc/passwd between line 7 and line 12
    > Your commands :

### 5. Bash Environment

#### Pitch
Figuring out the environment variables and their usage

#### Environment Variables
Environment variables are a way to influence the behavior of software on your system. For example, the environment variable "LANG" determines the language that the software uses to communicate with the user.

Variables are made up of names that are assigned values. For example, a French user's system should have the value "fr_FR.UTF-8" assigned to the "LANG" variable.

The meaning of an environment variable and the type of value that can be assigned to it are determined by the application that uses it. There are a small number of well-known environment variables, whose meaning and type of value are well determined, and which are used by many applications.

### 6. Process

#### Program VS Process
A process is a program that executes and that also has its ordinal counter, its registers and its variables; this is the subtlety between program and process. The difference between a process and a program is thin: the process has the program but also the current state of this one in the memory of the computer. The program is ultimately the set of files that, when executed, become the process.

#### What is a PID ?
A PID (that is, a process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system. A process is a running (i.e., executing) instance of a program. Each process is guaranteed a unique PID, which is always a non-negative integer.

Source: https://frameboxxindore.com/linux/what-is-pid-in-linux.html

### 7. Protocols and Servers

#### Pitch
Overview of server and internet protocols.

#### Goals
1. HTTP/HTTPS
    - Configure a virtual host
    - Deploy a one pager 
2. SSH 
    - Configure key-based authentication
3. SMB
    - Provide network shares to specific clients
4. TELENET
    - Install and configuration
5. FTP
    - Install and configuration

#### Exercices
> Connect to the virtual machine 10.12.181.X with the following credentials:  
> * ip : 10.12.181.X  
> * user : student  
> * password : student  

1.  On your kali (or other) , install ``ngnix`` to have an http server on port 8080. Replace the default page of ngnix by an html page displaying a hello world.
    > No answer required

1. What other well-known service could be used instead of nginx? 
    > Your answer : python, apache2

1. On your student machine, create a temporary http server with python, on port ``5000``. Then on your kali machine, open a browser and go to the address ``10.12.181.X:``.
    > Your command : python -m http.server 5000

1. Let's imagine that a hacker owns the domain name ``g00gle.com``, which tool would allow him to obtain an ssl certificate (https) very easily?
    > Your answer : Let's Encrypt

1. On a linux machine, what tool could you use to have a self-signed SSL certificate on your local machine (localhost) ? 
    > Your answer : openssl

1. On your student machine, install the ftp service and connect from your kali machine.
    > No answer required

1. What is the default port for ftp? 
    > Your answer : 21

1. Is the ftp protocol secured?
    > Your answer : no

1. On your student machine, install the telnet service and connect from your kali machine.
    > No answer required

1. What is the default port for telnet? 
    > Your answer :23

1. Is the telnet protocol secured?
    > Your anbswer : Telnet is vulnerable to network-based cyberattacks
    
1. Create a share file with samba between your Kali machine and your student machine.
    > No answer required

### 8. Downloading Files

#### Pitch
Learning how to transfer files between files different machines.

#### Exercices
1. On your Kali machine, create a file named malware.php.
    ````
    echo "This is a malware file" > malware.php
    ````
    Then, in the same directory, ccreate a temporary server with python on port 5000.
    ````
    python3 -m http.server 5000
    ````
1. On your Student machine, download the malware.txt file with the wget command.
    > Your command : wget 10.40.5.X:5000/malware.php

1. On your Student machine, download the malware.txt file with the cURL command.
    > Your command : curl 10.40.5.X:5000/malware.php --output malware.php

1. On the student machine, create a file named password.txt and transfer it to your kali machine with netcat
    > Your commands : touch password.txt
    > ON RECEIVING END : nc -l -p 1234 > password.txt
    > ON SENDING END : nc -w 3 [destination] 1234 < password.txt

1. On the student machine,  transfer ``/etc/passwd`` file to your kali machine with tftp
    > Your commands : 

### 9. Project

#### Context
The local library in your little town has no funding for Windows licenses so the director is considering Linux. Some users are sceptical and ask for a demo. The local IT company where you work is taking up the project and you are in charge of setting up a server and a workstation.
To demonstrate this setup, you will use virtual machines and an internal virtual network (your DHCP must not interfere with the LAN).


You may propose any additional functionality you consider interesting.

#### Must Have
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
    - A web-browser
    - **Required** 
        1. This workstation uses automatic addressing
        2. The /home folder is located on a separate partition, same disk
    - **Optional**
        1. Propose and implement a solution to remotely help a user
