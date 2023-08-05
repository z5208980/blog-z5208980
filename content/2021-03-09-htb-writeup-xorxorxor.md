---
title: "HTB Writeup - Xorxorxor"
date: "2021-03-09"
tags: ["HTB", "Crypto"]
image: ""
gradients: ["#30cfd0", "#330867"]
---

This blog is another something awesome blog, and I'll be doing another challenge from HTB. This time its about cryptography. The file required was challenge.py which was a python script that details the process how hoe the XOR encryption works. It generate a random key of length 4. It then XOR the flag of each byte with each byte of the key. The given flag for me, we given in the output.txt.

The key is to found the key instead of a random generate one in self.key. I noted that the key must be in length of 4. I was stumped trying to brute force and trying out tools, but I couldn’t get it. So I resorted to the forums which gave me a hint. The hint was that the flag started with these 4 characters HTB{. If we decipher HTB{ with the given output 134af6e1, we can would have found the key. So I wrote a script in python that turned the two in bytes and XOR them to obtain the 4 length key.

<details>
    <summary>Spoiler</summary>
    `Key: 5b1eb49a`
</details>

With the key found, what I did was changed the `decrypt()` function in`challenge.py` and changed the key to the required byte version of key and create the flag. It should print out the key! Hint: my`decrypt()` was exactly the same as the `encrypt()` provided.

Through this challenge I was able to learn a new cryptography for encryption, XOR. Since I was able to decipher a XOR encryption I did my research on its security. It seems that the security of Xor encryption depends on the key used to Xor the information. Just like this exercise I was able to determine that since the script use a key of length 4 and had some of the plain text given I would be able to construct the entire key and decipher the message. There are still many other encryption such as Blowfish or AES.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/191](https://www.hackthebox.eu/achievement/challenge/511926/191)