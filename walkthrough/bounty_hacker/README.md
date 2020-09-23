# Bounty Hacker

You talked a big game about being the most elite hacker in the solar system. Prove it and claim your right to the status of Elite Bounty Hacker!

## [Task 1] Living up to the title.

### #1 Deploy the machine.
```
No answer needed
```

### #2 Find open ports on the machine
```
No answer needed
```

### #3 Who wrote the task list? 
- With the nmap scan we know that anonymous FTP login is open
- login to FTP with username as `anonymous`
- we can see two files there `task.txt` which has the username and `locks.txt` which has the list of password

```
lin
```

### #4 What service can you bruteforce with the text file found?
- Again with nmap scan we can see the SSH service at port 22

```
SSH
```

### #5 What is the users password?
- With the gained creds above, we can brute-force SSH with metasploit's `auxiliary/scanner/ssh/ssh_login` module
- set the required `options` for the module, such as `RHOSTS`, `USERNAME` & `PASS_FILE`. Optionally set `VERBOSE` 
and `STOP_ON_SUCCESS` to `true`

```
RedDr4gonSynd1cat3
```

### #6 user.txt
- With the cracked ssh password, we can login now and retrieve the user flag

```
THM{CR1M3_SyNd1C4T3}
```

### #7 root.txt
- If we look for what programs user `lin` has permission to with `sudo -l`, we find that `lin` can execute 
`tar` as root. Bingo! That's our route to root.
- Searching on GTFOBins for `tar` and sudo access, we can see this 
`sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh`
- retrieve the flag at /root/root.txt

```
THM{80UN7Y_h4cK3r}
```
