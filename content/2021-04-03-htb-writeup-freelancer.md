---
title: "HTB Writeup - Freelancer"
date: "2021-04-03"
tags: ["HTB", "Web"]
image: ""
gradients: ["#AC32E4", "#4801FF"]
---

The previous web challenge was based of exploiting http request and extracting information from a website. For this one, I started if by viewing the source code for any hints. There was a commented out tag which contained a `.php` query. It was a `portfolio.php` that queries a `id` attribute. An `id=1`.

<img class="img-fluid" src="https://www.dropbox.com/s/cd5yzhegzzd1fdr/2021-04-03-htb-writeup-freelancer-1.png?raw=1">

I didn’t really know much SQL injection so I resorted to the forum and this time reddit, which told me to do **SQLmap**. A python language that automatics *SQLi*. Using the URL `http://domain/portfolio.php?id=1` I was able to go through founding that the person used the database freelancer and has a table `safeadmin` and `portfolio`. I used there `--current-db` and `--table` flag from *SQLmap* to figure out what was in the tables.

<details>
    <summary>Spoilers</summary>
Looking at the table safeadmin using the following command,
```bash
python3 sqlmap.py -u "http://domain/portfolio.php?id=1" -D freelancer -T safeadmin --dump
``` 
</details><br>

<img class="img-fluid" src="https://www.dropbox.com/s/odlc3gzkvishu7f/2021-04-03-htb-writeup-freelancer-2.png?raw=1">

I found a username and password. Now this seems very useful but where can I use it? There is a tool called **gobuster** (hinted from the HTB forum). It was a brute force tool that searches through the paths directory for a given website given a list of words to use from.

Using the command,
```bash
gobuster -u url -w common.txt
```

I was able to found a bunch of directories to the url. The most interesting ones are `/administrat` and `/mail`.

<img class="img-fluid" src="https://www.dropbox.com/s/4cdn3p38ljnfcsk/2021-04-03-htb-writeup-freelancer-3.png?raw=1">

The only reasonable one was `/administrat` which gave me a login page. I was correct as it loaded in a login form. I entered the values in, but unfortunately it was not correct. Maybe it was encrypted. I tried some password encryption methods but nothing. The forum did say not to crack the hash of credentials, so I that gave up. Next I tried again with gobuster on the `/administrat` route to check out all the sub directories it might include.

The only relevant route was the `panel.php`. I did a search about it and surely enough it seemed important. It was to handle the administration of MySQL over the web. After a long time of search, I was able to realise that I needed to read the url from the root folder of the web. That is `/var/www/html`. By doing so I was able to SQLi on the same thing which allowed me permission to read the files from `/administrat/panel.php` by redirecting from the root folder.

<details>
    <summary>Spoilers</summary>
```
python3 sqlmap.py -u "http://206.189.121.131:30651/portfolio.php?id=1" --file-read=/var/www/html/administrat/panel.php
```

This command basically allows me file privileges such as reading files. The command so dumps these information in a file located locally. 
</details><br>

<img class="img-fluid" src="https://www.dropbox.com/s/62l24px09ijx6vc/2021-04-03-htb-writeup-freelancer-4.png?raw=1">

Using sqlmap, I was able to read the file that was dumped locally. When I `cat` the local file, I was able to spot the flag. Finally. This challenge was very difficult and required a lot of time and learning.

This challenge was very hands on into SQL injection which was something new to me. I learnt a lot such as using tools to automate and speed up the process of collecting information about a webpage (**gobuster**) or database (**sqlmap**). In relation to security engineering, it is good practice to not include any code that isn’t meant to be in the production stage. It always good to have code separated from debugging and fixing and production. Just like in the case here, the commented out `a` tags allowed me to perform SQLi injections knowing that there was a `.php` file that queries some sort of database. Even through I couldn’t get the flag out of it, I was able to found a lot of information such as getting the database from just the source page.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/82](https://www.hackthebox.eu/achievement/challenge/511926/82)