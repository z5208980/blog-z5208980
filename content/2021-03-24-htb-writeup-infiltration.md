---
title: "HTB Writeup - Infiltration"
date: "2021-03-24"
tags: ["HTB", "OSINT"]
image: ""
gradients: ["#360940", "#38f9d7"]
---

This challenges was different to the traditional download files type of challenge I usually get. Since there was nothing, the only information that could get me a lead was the description of the challenging. It displays, *Can you find something to help you break into the company 'Evil Corp LLC'. Recon social media sites to see if you can find any useful information.* I guess that could only mean analysing data on public sources such as the *internet* and Google.

<img class="img-fluid" src="https://www.dropbox.com/s/fvo4cszu0jdd3a1/2021-03-24-htb-writeup-Infiltration-1.png?raw=1">

Upon searching **Evil Corp LLC**, the first site was the social media site LinkedIn. I wasn't logged in LinkedIn at the time and was too ceebs to do so. This meant I couldn't access their profile page, due to LinkedIn's authwall protection. Luckily, Google displays the bio as the description for the link which happens to contain a `HTB{}` flag.

<img class="img-fluid" src="https://www.dropbox.com/s/0lksms5lanflvp5/2021-03-24-htb-writeup-infiltration-2.png?raw=1">

At first I was skeptical that I found the flag and it seemed too good to be true. Yes, it was too good to be true. The submission for the flag was rejected. I resorted to continue my search on **Google** by going through the links on the query. The next one was an Instagram. I tried analysing the pictures but nothing. So I tried the third site. Another in **Instagram** post and this time my good eyes from the challenge *Cat* instantly spotted a HTB in the image. Not sure if this was a legit flag but it always worth the try and what do you know? It was the *flag*.

**Social media** data is usually public on the internet, whether it is personal information, such like hobbies, dob and connections or post or image of friend and family. This can cause identify vulnerabilities, used for things like social engineering, or identify theft. **Open Source Intelligenc**e is a field dedicated to collecting data and information on open publicly available sources. Like in this challenge, I was able to found information such as who works for Evil Corp LLC and their professions, what devices they are using, and other useful information (in my case the flag!). I am not sure if I'm a pro now or some of these challenges are far too easy. So for my next attempt, I'm going to try a harder one. Hopefully it'll make me spends days trying to figure out.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/83](https://www.hackthebox.eu/achievement/challenge/511926/83)