# Tartarus

This is a beginner box based on simple enumeration of services and basic privilege escalation techniques. Based Jake

#### This CTF is from https://tryhackme.com/

## [Task 1] Tartarus
User and Root Flag

#### Nmap 
Start with the simple Nmap scan
- we see the `anonymous` FTP open

#### FTP
- FTP'd with username/password`anonymous`
- initially we dont find anything here
- but if you do `ls -la`, you will see a wierd directory called `...`
- CD to it
- another `...`
- CD again into it
- we find the file `yougotgoodeyes.txt`
- downloading it and seeing its content gives use a directory call `/S3...` (not shown full) which is login form

#### GoBuster
`gobuster dir -u http://<IP>/ -w /opt/wordlists/wordlists/dirb/common.txt -q -t 25 -x php,html,txt`
- this shows robots.txt
- opening robots.txt, reveals `admin-dir`
- navigate to that directory, gives two files `userid.txt` & `credentials.txt`

#### Hail Hydra!
`hydra -L userid.txt -P credentials.txt <IP>  http-post-form "/sUp3r-s3cr3t/authenticate.php:username=^USER^&password=^PASS^:F=incorrect" -V | tee hydra.log`

#### Reverse Shell
- after logging in we see a upload form. To which we can upload php files as well.
- grab any php reverse shell (https://github.com/pentestmonkey/php-reverse-shell) and change the IP and PORT to yours
- upload and gain the reverse shell

## #1 User Flag
- grab the user flag in d4rckh directory

#### Stablize the shell (optional)
1. `python -c 'import pty; pty.spawn("/bin/bash")'`

2. `stty raw -echo; fg` (for zsh)

3. `stty rows <rows value> columns <column value>` (get the values with `stty -a`)

4. `export TERM=st-256color` (your term might be different if not ST terminal)

5. `exec /bin/bash`

```
0f7dbb224....
```

### #2 Root Flag    
- Enumerate with linpeas.sh
- get to see a cron job that executes `cleanup.py` which in turn executes system commands as root
- you can gain root shell in many ways and I used `chmod +s /bin/bash`. This will set the SUID for bash without dropping 
root priv
- after waiting 30seconds, and running `/bin/bash -p` we are root

```
7e0558121....
```

