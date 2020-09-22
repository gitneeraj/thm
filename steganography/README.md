## CC: Steganography
 
A crash course on the topic of steganography

## [Task 1] Intro
All needed files can be found inside the included zip file

```
No answer needed
```

## [Task 2] Steghide

### #1 What argument allows you to embed data(such as files) into other files?
```
embed
```

### #2 What flag let's you set the file to embed?
```
-ef
```

### #3 What flag allows you to set the "cover file"?(i.e  the jpg)
```
-cf
```

### #4 How do you set the password to use for the cover file?
```
-p
```

### #5 What argument allows you to extract data from files?
```
extract
```

### #6	How do you select the file that you want to extract data from?
```
-sf
```

### #7 Given the passphrase "password123", what is the hidden message in the included "jpeg1" file.
```
$ steghide --extract -sf spect/jpeg1.jpeg -xf jpeg1_message.txt -p "password123"
$ cat jpeg1_message.txt

pinguftw
```

## [Task 3] zsteg

### #1 How do you specify that the least significant bit comes first
```
--lsb
```

### #2 What about the most significant bit?
```
--msb
```

### #3How do you specify verbose mode?
```
-v
```

### #4 How do you extract the data from a specific payload?
```
-E
```

### #5 In the included file "png1" what is the hidden message?
```
$ zsteg spect/png1.png

nootnoot$
```

### #6 What about the payload used to encrypt it.
```
b1,bgr,lsb,xy
```

## [Task 4] Exiftool

### #1 In the included jpeg3 file, what is the document name
```
$ exiftool spect/jpeg3.jpeg

Hello :)
```

## [Task 5] Stegoveritas

### #1 How do you check the file for metadata?
```
-meta
```

### #2 How do you check for steghide hidden information
```
-steghide
```

### #3 What flag allows you to extract LSB data from the image?
```
-extractLSB
```

### #4 In the included image jpeg2 what is the hidden message?
```
$ stegoveritas -steghide spect/jpeg2.jpeg
$ cd results/
$ strings steghide_9a2e9d2b6f888b365327dfa79142c701.bin

kekekekek
```

## [Task 6] Spectrograms

### #1 What is the hidden text in the included wav2 file?
```
Google
```

## [Task 7] The Final Exam

Good luck and have fun!

### #1 What is key 1?
```
$ strings final_exam/exam1.jpeg
password=admin

$ steghide --extract -sf final_exam/exam1.jpeg -xf exam1_key1_txt -p "admin"
$ cat exam1_key1_txt

superkeykey
```

### #2 What is key 2?
```
The hidden text/url in audio file is "https://imgur.com/KTrtNI5"

$ zsteg final_exam/KTrtNI5.png

fatality
```

### #3 What is key 3?
```
My approach
 - download the qrcode
 - in GIMP change colors to black and white
 - scan the qrcode.
 
killshot
```










