---
title: "HTB Writeup - Impossible Password"
date: "2021-03-08"
tags: ["HTB", "Reversing"]
image: ""
gradients: ["#85FFBD", "#FFFB7D"]
---

Welcome to my first Something Awesome Project and my first HackTheBox Challenge. This was my attempt at solving a challenge on HTB so here my walkthrough on how I solved the Impossible Password.

The file required for this challenge was a binary executable called, `impossible_password.bin`. The script ran as the picture showed below. It seems like the copies my input and prints within `[]`. I research on HTB that a hint was to use `ltrace` and a software called Radare2. I sort of knew what ltrace does and tried it out. ￼

<img class="img-fluid" src="https://www.dropbox.com/s/ed149evtyhm6e9e/2021-03-08-htb-writeup-impossible-password-1.png?raw=1">

I appears it was using `scanf` and `strcmp` to compare my input to the string `SuperSeKretKey`, then exited. So I ran the script again with SuperSeKretKey. I was able to go onto the next stage which was printing `**` and an `scanf`. I tried a random string again and a bunch of command came up.

<img class="img-fluid" src="https://www.dropbox.com/s/e5t39p3c2hiy1ao/2021-03-08-htb-writeup-impossible-password-2.png?raw=1">

It appears that it comparing to the the password `3_G}S[l<=)js\\:X;F52\` so I tried entering that again and this is what it output. 

<img class="img-fluid" src="https://www.dropbox.com/s/qh4cl8avuj8k4hj/2021-03-08-htb-writeup-impossible-password-3.png?raw=1">

The compared string seemed to have changed. I was able todo some research on **Radare2**. Radare2 was a reverse engineering software which allowed me to view its assembly code. To use `radare2,radare2 -w -A ./impossible_password.bin`

```bash
s main # seeks the main function
pdf # print the disassembly of the current function
```

To keep things short and without revealing the solution, I’ll try explain this part of the output command. Looking at the code address `0x0040094a` since to be an arg valued at 20. This was the number of times that the rand function execute so I assume the function call at `0x0040094f` contains `time`, `malloc` and `rand`. I think the most important is at `0x00400961` where the strcmp was comparing to a changing string. Going I few lines down, `0x00400968` since to jump to leave and ret explaining why is exited and not executing address `0x0040096a`. I was also to change the jump address to `0x0040096a` via a few commands so that it would execute and hopefully run the output for the flag.

<img class="img-fluid" src="https://www.dropbox.com/s/bhkwh7o77lx78nt/2021-03-08-htb-writeup-impossible-password-4.png?raw=1">

When running the file again. I was able to get the flag!

<img class="img-fluid" src="https://www.dropbox.com/s/69p7ftt0jv5iu6t/2021-03-08-htb-writeup-impossible-password-5.png?raw=1">

This was was suppose to be easy, but I found it pretty difficult, nevertheless with the help of the internet and forums, I was able to solve it. Some useful concepts I've learnt was being able to reverse engineering a script without necessary changing the code. I was able to use a Radare2 a reverse engineering tool and got my first HTB flag!

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/26](https://www.hackthebox.eu/achievement/challenge/511926/26)