---
title: "HTB Writeup - Digital Cube"
date: "2021-03-16"
tags: ["HTB", "Stego"]
image: ""
gradients: ["#f5f7fa", "#c3cfe2"]
---

This one was fairly straight forward, so I don’t think I’ll be writing much in today’s something awesome. The required file was `digitalcube.txt` which was a text file with 0s and 1s. The only thing you can do is to convert to ASCII or Image. So I first did a binary to ASCII conversion.

<img class="img-fluid" src="https://www.dropbox.com/s/99tigonkt5fecea/2021-03-16-htb-writeup-digital-cube-1.png?raw=1">

Turn out the conversion was a bunch of random numbers which I don’t think gave any meaning. So I tried conversion of the binary to image.

<img class="img-fluid" src="https://www.dropbox.com/s/vzv6496uaihr4hq/2021-03-16-htb-writeup-digital-cube-2.png?raw=1">

This time it seems to have generated a QR code. With this I used an online tool to scan the code and it gave in the flag.

<img class="img-fluid" src="https://www.dropbox.com/s/s0bxabuvx7u0mp2/2021-03-16-htb-writeup-digital-cube-3.png?raw=1">

I should have known straight away that I need to convert to image because the challenge type was stego. …

Although this one was fairly simple. It was cool how we can hide information within another message. Just like using binary to hide the QR code. You can store message in other form such as video or even audio. Welcome to the world of steganography in cyber security. It very important that it relates to security engineering because it ensure that our data is encrypted in a medium to conceal and deceive. It a cheap and sneaky way to store information without the need of keys or cryptography.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/24](https://www.hackthebox.eu/achievement/challenge/511926/24)