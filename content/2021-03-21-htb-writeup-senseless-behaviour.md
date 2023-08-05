---
title: "HTB Writeup - Senseless Behaviour"
date: "2021-03-21"
tags: ["HTB", "Stego"]
image: ""
gradients: ["#43e97b", "#38f9d7"]
---

Senseless Behaviour was a challenge that was long and time consuming (for me at least). It wan't difficulty as it just figuring out the many steganography techniques used for each medium (in this case `.wav`, `.png` and the **braille language**. The file given was `meow.wav`. It was an audio file that played the theme song for Nyan Cat. Cute!

Not knowing much about audio files. I did a search on audio steganography and found a useful site with a lost tools to help. I used the first steganography tool called **stegohide**. The program ran as, `python steg_brute.py -b -d password.txt -f file`. What I got out of it was `password.txt` was a list of password. A file needed was a list common words. The most popular one was `rockyou.txt`. Wow, this mean time to brute force the audio.

The script should brute force and create a `meow_flag.txt` which is a VERY large file. When I opened the large file, it was just a bunch of texts. The first few characters `ODk1MDRlNDcwZDBhMWEwYTAwMDAwM` looked like it was in base64. Converting into ASCII could reveal maybe a text with the flag. Using an online **base64** to ASCII converter, it decoded to `89504e470d0a1a0a0000000d49` which was something else. This time (after doing previous challenges) I easily recognise this was in **hex**. Using another converter from hex to ASCII maybe it'll reveal the true text.

<img class="img-fluid" src="https://www.dropbox.com/s/zuwxypddyifehii/2021-03-21-htb-writeup-senseless-behaviour-1.png?raw=1">

But it turned out to be gibberish. However, there was a massive clue stating that maybe I needed to convert the file to `.png`. So I use my skills in the terminal to convert my `meow_flag.txt` into a `.png` through this command. 

```
cat meow_flag.txt | base64 | xxd -r -p &gt&semi; img.png
```

<img class="img-fluid" src="https://www.dropbox.com/s/2jpeltvhcrnt3um/2021-03-21-htb-writeup-senseless-behaviour-2.png?raw=1">

First I thought it might of being physical hidden in the image, but I couldn't spot it. Since I've done I a lot deciphering of different format, I think I needed to do another steganography. Again thanks to research, I was meant to use a steganography technique to extract information about the image. I manages to found this online steganography tool in which I just tried all the possible filters. The only one that made most sense was the **Bit Planes**.

<img class="img-fluid" src="https://www.dropbox.com/s/ltrdd3gg11h64aj/2021-03-21-htb-writeup-senseless-behaviour-3.png?raw=1">

At this point, it was obviously a braille message. I simply use an online braille converter, inputted in the characters and it revealed the flag. I was finally done.

<img class="img-fluid" src="https://www.dropbox.com/s/bmp8dtc531jbkmj/2021-03-21-htb-writeup-senseless-behaviour-4.png?raw=1">

This stego challenge was much harder, as I know nothing about audio stenography. It took way too long to try out, but atleast it was a complete 180 to the previous challenges I attempted. it just goes to show how many ways stenography can be stacked on to hide a message. The more steganography method use to hide the message, the longer and less time and feasibility it'll take for the hacker to try the many ways and techniques in order to decode it correctly. In term of security, it a good confidentiality technique to for data. Next week, I'll be doing OSINT.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/58](https://www.hackthebox.eu/achievement/challenge/511926/58)