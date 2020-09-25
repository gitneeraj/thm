# Lian_Yu
 
A beginner level security challenge

#### This CTF is from https://tryhackme.com/

## [Task 1] Find the Flags
Welcome to Lian_YU, this Arrowverse themed beginner CTF box! Capture the flags and have fun.

### #1 Deploy the VM and Start the Enumeration.
```
No answer needed
```

### #2 What is the Web Directory you found?

Initial scan with `gobuster dir -u http://<IP>/ -w /opt/wordlists/directory-list-2.3-small.txt | tee  gobuster/gobuster_island.log`
would give use a hidden directory called `/island`. Enumerating this directory further we get what we need.

```
$ gobuster dir -u http://<IP>/island -w /opt/wordlists/directory-list-2.3-medium.txt | tee  gobuster/gobuster_island.log

2100
```

### #3 what is the file name you found?

- From the above enum we got the directory called `2100`. Checking the source code we see the following comment
`<!-- you can avail your .ticket here but how?   -->` which points to us the file with `.ticket` extension.

- Now we can further enumerate this directory for that particular file extension

```
$ gobuster dir -u http://<IP>/island/2100 -w /opt/wordlists/directory-list-2.3-medium.txt -x "ticket" | tee  gobuster/gobuster_island.log

green_arrow.ticket
```

### #4 what is the FTP Password?
- Visting the link `/island/2100//green_arrow.ticket` we get to see the hashed password. At first it seems to be base64, but its not.
- If you directory pasting this on google you will get to know the hash type. Surpirsingly its base58 (Honestly I am hearing it for first time)
- You can decode it online

```
!#th3h00d
```

#### Now the first part of the fun starts - 
- login to FTP with username `vigilante` and password from above
- we have bunch of files here.
- download them all
- Clearly we can see that `Leave_me_alone.png` is the one we need to approach.
- but it seems to be broken. I mean checking it with `exiftool` says `file format error`
- after a lot of spending time, I figured out that its magic headers may be corrupt. So opened it with `hexedit`
- It seems we are correct. We need to fix the magic headers for PNG file.
- I replaced the beginning of the file with `89 50 4E 47 0D 0A 1A 0A`
- This reveals the password. But for what??
- Ah! again after spending some time, understood that it might be the password for the file `aa.jpg`
- Extracting it with the password gives zip file.
- Extract the zip file, gives the password for SSH. Because we know thats the next question in line :)

### #5 what is the file name with SSH password?
```
shado
```

####  Second part of the fun...
- We have the password from `shado` file. But whats the SSH username??
- After spending some mre time...
- FTP'd back to the machine.
- checking the `/home` directory reveals two users `vigilante` AND `slade`
- Bang! thats the username for our SSH

### #6 user.txt
- SSH with `slade` and password found in `shado` file

```
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
```

### #7 root.txt
- I guess the author did not wanted to make this hard. So a simple privesc with `pkexec` is available.
- https://gtfobins.github.io/gtfobins/pkexec/#sudo

```
THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
```
