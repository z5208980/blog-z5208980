---
title: "HTB Writeup - Flippin Bank"
date: "2021-03-13"
tags: ["HTB", "Crypto"]
image: ""
gradients: ["#30cfd0", "#330867"]
---

This third challenge was way more difficult in term of understanding but been able to understanding crypto is very rewarding. The challenge is trying to found the byte that was flipped into order to found the correct cipher text. It required me to use the concept of block chaining which I’ll try to simply explain below.

The message encrypted is this variable msg which has 96 bytes. We can leak the cipher text by displaying an incorrect user/pass. I’ve changed the user admin to bdmin since it’ll be easier todo the decrypt of the blockchain. Note that the b in bdmin is at the 17 bytes meaning there are is in 16 bytes sequences. Here is a very useful site I found about cipher block chaining linked here). I’ll try to apply it here.

So the encryption that two 16 bytes and XOR to create the cipher. That is

```
AAAAAAAAAAAAAAAA (IV Key)
^
BBBBBBBBBBBBBBBB (plain_text)
----------------
CCCCCCCCCCCCCCCC (cipher_text)

then the next cipher takes the previous text,

CCCCCCCCCCCCCCCC (previous cipher_text as key)
^
DDDDDDDDDDDDDDDD (plain_text)
----------------
EEEEEEEEEEEEEEEE (cipher_text)

and this continues if there is more text to chain
```

As you can see we are taking the previous cipher as our key to XOR the next sequence of bytes. This process is the block chaining. Hence, we need to do, found the B given A and C. So our leaked cipher text is split into 16 hens are `f67e883f8f4c8d4d01c2e7f283d795cb669` and `ca064dd;`. Notice the ca is the changed b in bdmin mentioned above. We need to change it to a for admin to so we need to XOR the first hex of the 16 bytes.

So doing this in python,

```py
0xca ^ B = 0x62 # 0x62 = b in hex

B = hex(0xca ^ 0x62) # 0x94

A ^ 0x94 (B) = 0x61 # 0x61 = a in hex

A = hex(0x94 ^ 0x61)
And there is the flag. Luckily this challenge was simple with just a byte flip to get the answer.
```

Upon more research Cipher block chaining (CBC) is a good way to chain information and ensure it **integrity**. It seems to have a very similar concept to block chaining in cryptocurrency. This was a very interesting cryptography challenge. Next week, I’ll be moving to stego challenges.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/124](https://www.hackthebox.eu/achievement/challenge/511926/124)