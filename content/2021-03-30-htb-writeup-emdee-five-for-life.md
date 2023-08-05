---
title: "HTB Writeup - Emdee Five for Life"
date: "2021-03-30"
tags: ["HTB", "Web"]
image: ""
gradients: ["#8EC5FC", "#E0C3FC"]
---

This week is all about exploiting on the web. This was a very important challenge as it allowed me to see what people can do behind the scene when I’m using a website or creating one. HTML forms can easily be manipulated with scripts and without really being on the webpage itself. This was a challenge I really enjoyed because it showed me how vulnerable websites can be.

When I created an instance on HTB the url redirected me to a simple html page where I had to input the MD5 hash value to a given string. However, whenever I entered the string into the input and submitted it, the webpage displayed a `Too Slow!` message. No matter how fast I tried, I was just `Too Slow!`.

<img class="img-fluid" src="https://www.dropbox.com/s/ytzrw9sgztn8e6n/2021-03-30-htb-writeup-emdee-five-for-life-1.png?raw=1">

It seemed that doing it by hand was no feasible and hence the only way I could possibly make it work was to probably write a script that can immediately trigger a request to the address, get the string and convert the MD5 before entering it by a `POST` request to the page. This was perfect in python. I will not post the script I wrote but I will write how I managed to solve it.

```py
import requests
import re
import hashlib
```

Theses were three libraries necessary for the script. **requests** was used to retrieve (`.get`) and post (`.post`) http requests from the webpage url. With the html retrieved I need to use **re** to extract an expression that contained the string. To easily convert the string to a MD5 hash value, the **hashlib** contained a function that can help with that. An extra hint is to also use a `.session()` for the request, or else the content with refresh and not work. These were all the stuff required (for me) to capture the flag for this challenge.

This challenge was just right in terms of difficulty, as I knew what to do and how to do it. Essentially I advanced my learning on how to exploit and extract information from a website through simple scripting. In relation to security engineering, I would have to say that webpages can be very volatile as in scripts can be used to access and submit information without being on the webpage itself. This should be also good to keep the method of request secure from attack like DDOS and injections.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/67](https://www.hackthebox.eu/achievement/challenge/511926/67)