# The Cod Caper
 
A guided room taking you through infiltrating and exploiting a Linux system.

## [Task 1] Intro
```
No answer needed
```


## [Task 2] Host Enumeration

### How many ports are open on the target machine?
```
2
```

### What is the http-title of the web server?
```
Apache2 Ubuntu Default Page: It works
```

### What version is the ssh service?
```
OpenSSH 7.2p2 Ubuntu 4ubuntu2.8
```

### What is the version of the web server?
```
 Apache/2.4.18
```


## [Task 3] Web Enumeration

### What is the name of the important file on the server?
```
administrator.php
```


## [Task 4] Web Exploitation

### What is the admin username?
```
pingudad
```

### What is the admin password?
```
secretpass
```

### How many forms of SQLI is the form vulnerable to?
```
3
```


## [Task 5] Command Execution

### How many files are in the current directory?
```
3
```

### Do I still have an account
```
yes
```

### What is my ssh password?
```
pinguapingu
```


## [Task 6] LinEnum

### What is the interesting path of the interesting suid file
```
/opt/secret/root
```



## [Task 7] pwndbg
```
No answer needed
```


## [Task 8] Binary-Exploitaion: Manually
```
No answer needed
```


## [Task 9] Binary Exploitation: The pwntools way
```
No answer needed
```


## [Task 10] Finishing the job

### What is the root password!
```
$ hashcat -m 1800 \$6\$rFK4s/vE\$zkh2/RBiRZ746OW3/Q/zqTRVfrfYJfFjFc2/q.oYtoF1KglS3YWoExtT3cvA3ml9UtDS8PFzCk902AsWx00Ck. /opt/wordlists/rockyou.txt

love2fish
```


## [Task 11] Thank you!
```
No answer needed
```