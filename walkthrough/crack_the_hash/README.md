# Crack the hash

Cracking hashes challenges

## [Task 1] Level 1
Can you complete the level 1 tasks by cracking the hashes?

### #1 48bb6e862e54f2a795ffc4e541caed4d
```
$ hashcat -m 0 "48bb6e862e54f2a795ffc4e541caed4d" /opt/wordlists/rockyou.txt

easy
```

### #2 CBFDAC6008F9CAB4083784CBD1874F76618D2A97
```
$ hashcat -m 100 "CBFDAC6008F9CAB4083784CBD1874F76618D2A97" /opt/wordlists/rockyou.txt

password123
```

### #3 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032
```
$ hashcat -m 1400 "1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032" /opt/wordlists/rockyou.txt

letmein
```

### #4 $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom
```
$ hashcat -m 3200 "\$2y\$12\$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom" /opt/wordlists/rockyou.txt

bleh
```

### #5 279412f945939ba78ce0758d3fd83daa
```
$ hashcat -m 900 "279412f945939ba78ce0758d3fd83daa" /opt/wordlists/rockyou.txt

NOTE: this is not present in default rockyou wordlist. So I used crackstation.net to decode it online

Eternity22
```

## [Task 2] Level 2

### #1 Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85
```
$ hashcat -m 1400 "F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85" /opt/wordlists/rockyou.txt

paule
```

### #2 Hash: 1DFECA0C002AE40B8619ECF94819CC1B
```
$ hashcat -m 1000 "1DFECA0C002AE40B8619ECF94819CC1B" /opt/wordlists/rockyou.txt

n63umy8lkf4i
```

### #3 Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.

Salt: aReallyHardSalt

Rounds: 5
```
$ hashcat -m 1800 "\$6\$aReallyHardSalt\$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02." /opt/wordlists/rockyou.txt

waka99
```

### #4 Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6

Salt: tryhackme
```
$ hashcat -m 160 "e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme" /opt/wordlists/rockyou.txt

481616481616
```




