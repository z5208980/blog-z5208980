---
title: "HTB Writeup - Easy Phish"
date: "2021-03-26"
tags: ["HTB", "OSINT"]
image: ""
gradients: ["#ed6ea0", "#ec8c69"]
---

Since I really liked the previous OSINT challenge, I tried again with another that didn't require any files. This was only worth 20pts so I assume was going to be easy. The descriptions is *Customers of secure-startup.com have been recieving some very convincing phishing emails, can you figure out why?*

I first thing I did was search up `secure-startup.com` but that didn't help. It directed me to some useless site that didn't give any information or leads. Then using my networking skills I tried to obtain authoritative nameservers, with `whois`. I needed information about their email system, so what I needed to do was to think of the different email authentication protocols and try them out. The most common ones were **SPF** and **DMARC**.

Sender Policy Framework (SPF) is a system that allows approved senders to send email on the behalf of the other domain server. It is used to determine if the receiving email is authorised for sending on the domain. To implement SPF records, it only requires a TXT entry in DNS. So I queried `http://secure-startup.com` with `nslookup` to check for any `-type=txt` records. And there was, though it was only the first half of the flag. It seems like I'm on the right track.

DMARC is a standard used with SPF and Domain Keys Identified Mail (DKIM) to check the legitimacy of a sent email. IT validate and domain by checking where it is **FROM**, and uses a txt type record. The other half comes from `secure-startup.com`, so which to monitor DMARC requires a `-type=txt` record. Querying the DMARC reveal the other half.

Here is a usefully site) that got me through this challenge.

This challenge was unique in the why I learnt about the different protocols in emails. I was able learn that emails can be spoof and be created so that the email came from a legit organisation. Luckily there are protocols that can help determine if a email is legit or not, through **SPF**, **DKIM** and **DMARC**. In relation to security engineering, spoofing email is a form of social engineering known as phishing. This security course has talked about phishing emails and how to prevent and detect it but not on a technical level. Preventing spam and avoid getting malware on device through an email is very important in security engineering.

Here is the proof I solved this challenge. [https://www.hackthebox.eu/achievement/challenge/511926/79](https://www.hackthebox.eu/achievement/challenge/511926/79)