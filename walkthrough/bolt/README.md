# Bolt
 
A hero is unleashed

## [Task 1] Deploy the machine
```
No answer needed
```

## [Task 2] Hack your way into the machine!

### #1	What port number has a web server with a CMS running?
```
$ nmap -v -sC -sV -oN nmap/initial <IP>

8000
```

### #2 What is the username we can find in the CMS?
```
TIP: Check the comments post on the website http://<IP>:8000

bolt
```

### #3 What is the password we can find for the username?
```
TIP: Check the comments post on the website http://<IP>:8000

boltadmin123
```

### #4 What version of the CMS is installed on the server? (Ex: Name 1.1.1)
```
TIP: Google and find the admin login page for cms. Then with the above creds login to find the version in footer

Bolt 3.7.1
```

### #5 There's an exploit for a previous version of this CMS, which allows authenticated RCE. Find it on Exploit DB. What's its EDB-ID?
```
48296
```

### #6 Metasploit recently added an exploit module for this vulnerability. What's the full path for this exploit? (Ex: exploit/....)
```
exploit/unix/webapp/bolt_authenticated_rce
```

### #8 Look for flag.txt inside the machine.
```
THM{wh0_d035nt_l0ve5_b0l7_r1gh7?}
```

