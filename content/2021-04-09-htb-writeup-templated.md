---
title: "HTB Writeup - Templated"
date: "2021-04-09"
tags: ["HTB", "Web"]
image: ""
gradients: ["#007adf", "#00ecbc"]
---

This challenge was a very enjoyable one as I got a taste of **web server injection**. When I launched the instance, I was confronted with this page.

<img class="img-fluid" src="https://www.dropbox.com/s/6jrihef627nya4q/2021-04-09-htb-writeup-templated-1.png?raw=1">

At first I didn't know how to approach this. The only thing I know is that the website was powered with Flask and Jinja2. That is it will be written python. There was nothing I could do with this website. It was a simple html. I then resorted to the forum saying something about SSTI. SSTI stands for **Server Side Template Injection**. That made sense because the name of this challenge was called templated.

I searched what SSTI was about. It was basically using the **native templating syntax** to inject payload (commands, sql) into the template so the server can execute and return the information. I have using Flask and Jinja2 before so I knew there syntax was using `{{ }}`.

The guide here demonstrate on Django using the template engine Jinja2, with `{{7*7}}`

<img class="img-fluid" src="https://www.dropbox.com/s/7qskcabpa2fyak3/2021-04-09-htb-writeup-templated-2.png?raw=1">

It worked! We can see that `7*7` return `49` on the webpage. It was simply from here on. Looking for Jinja2 SSTI, I was able to found this page which contain the line of code I was looking for.

<details>
    <summary>Spoilers</summary>
    ```py
    {{request.application.__globals__.__builtins__.__import__('os').popen('ls').read()}}
    ```
    This code is essentially a `ls` command to get the web server files.
</details><br>

By using the injection payload and simple linux commands, I was about to navigate to the flag file and look inside of it. The flag appeared and I was done.

<img class="img-fluid" src="https://www.dropbox.com/s/ywuoyss1zpilmdj/2021-04-09-htb-writeup-templated-3.png?raw=1">

This challenge in a security engineering looking at the a form of security vulnerability in web servers known as **SSTI**. Attackers can use malicious inputs to a web template and execute commands on the server. This leads to *remote code execution (RCE)* which is another web application vulnerability. Best practices to protect against these is to use **character-escaping** functions to ensure the inputs are valid for execution and not just any query or command. You can also use something called **Web Application Firewall (WAF)**. This is used to monitor, traffic and identify any unusual patterns. Overall this challenge had the right level of difficulty that wasn't too time consuming and I learn't something.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/152](https://www.hackthebox.eu/achievement/challenge/511926/152)