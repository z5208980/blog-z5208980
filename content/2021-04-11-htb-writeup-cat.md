---
title: "HTB Writeup - Cat"
date: "2021-04-11"
tags: ["HTB", "Mobile"]
image: ""
gradients: ["#CBBACC", "#2580B3"]
---

I am back for another writeup of my Something Awesome Project. This time I'll be exploring mobile challenges. This challenge was a piece of cake. I’m not sure what I was meant to learn out of it expect being able to extract an `.ab` file and understanding the structure of an *Android's application*.

The file required to start the challenge is `cat.ab`. Not knowing what `.ab` was I googled the file extension. It turns out to be an **Android Backup** file. They are to be used to backup application project using the Android SDK software. More details can be read [here](https://www.reviversoft.com/file-extensions/ab).

I guess the next thing to do is to open it. This was so simple, using the power of Google again, I search on how to extract a `.ab` file. If you can’t found it then I guess the spoiler will do the trick.

<details>
    <summary>Spoilers</summary>
    `( printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" tail -c +25 cat.ab ) |  tar xfvz -`
</details><br>

The extraction should give you two folders. One of the folders opened up to many more folders with `_manfest` files. SPOILERS: If you don’t want to waste your time like I did don’t bother with them. The other folder however contained something I was looking for.

Though I didn't spend a lot of time researching android materials, and .ab files. I think one reason here is to not overthink. Sometime the answer can be hard to spot but not does not involve complex procedures. In relation to security engineering being able to hide information is important. One of the method is through picture and image, but like I mention in my introduction, this challenge was a challenge that could be used as a warmup.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/115](https://www.hackthebox.eu/achievement/challenge/511926/115)