---
title: "HTB Writeup - M0rsarchive"
date: "2021-04-07"
tags: ["HTB", "Misc"]
image: ""
gradients: ["#00989b", "#005e78"]
---

I wasn’t too sure what the Misc challenges were about but I managed to solve this one. Upon unzipping the folder, I was presented with a image called `pwd.png` and `flag_999.zip` which was password protected. This could only mean the information in the image was the key to unzipping the folder. Looking at the image. It was very small.

<img class="img-fluid" src="https://www.dropbox.com/s/zgia9nduj55djj5/2021-04-07-htb-writeup-m0rsarchive-1.png?raw=1">

I think by using it small size I could just read the pixels on the image and determine if it was a line or a dot, which was the only strokes to morse code. So I wrote a function that converted an image to morse code called `img_to_morse()`. The `pwd.png` outputted 9. I entered it in and unzipped the folder. It worked so that meant I was on the right track, however it appeared to be another image format morse code and a password protect zipped folder called `flag_998.zip`. I could only assume at this point it was an attempt to solve the morse code as the password and unzipping the folder recursively **998** more times.

Luckily in **python** this was manageable. My approach in pseudo code was,
```py
for i in range(999, 0, -1)
    morse = img_to_morse(img)
    password = decode_morse(morse)
    unzip(folder_i, password)
    # To prevent flooding of folder in my directory by deleting prev stuff
    remove(pwd.png, flag_i-1.png)
```

I just need to loop through the `i` and determine the password to unzip the folder. Then to avoid creating 1000 images and folder, I removed the previous one that I cracked. The entire script for me ran for 511.46 seconds. To provide a hint for my script that I wrote, these were the libraries I used.

```py
from PIL import Image # process pwd.png image
from zipfile import ZipFile # used to unzip in python

from os import chdir, remove, rmdir # mange directory
```

I just found a simple morse code encoder and decoder on GitHub to assist me obtaining the password.

<img class="img-fluid" src="https://www.dropbox.com/s/0qte7i7w1onljjb/2021-04-07-htb-writeup-m0rsarchive-2.png?raw=1">

I couldn’t really found a security concept related to this challenge, but I feel like it’s cryptography or stenography. Either way this was a tedious method to store and secure data if the attacker tries to manually hack this folder. The process of hiding and adding a layer of protection feature an x amount time does seem like a reasonable way of being safe. Maybe an improvement to this and making it more difficult is changing up the image to stuff like a QR code, braille language or a simple encryption text. That way it would be deem very annoying to implement and decipher each folder. I guess a large involvement is also scripting like many of the other challenges I did. Python is such a powerful language, that can be utilised to translate hidden information and manipulate files.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/98](https://www.hackthebox.eu/achievement/challenge/511926/98)