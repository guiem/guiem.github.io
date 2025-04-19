---
id: 760
title: 'How To Set Up Apache Virtual Hosts on Ubuntu'
date: '2013-09-28T17:28:52+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=760'
permalink: /how-to-set-up-apache-virtual-hosts-on-ubuntu/
categories:
    - programming
---

\[this post will be properly edited\]

`<br></br>sudo mkdir -p /var/www/example.com/public_html<br></br>sudo chown -R $USER:$USER /var/www/example.com/public_html<br></br>sudo chmod -R 755 /var/www<br></br>sudo cp /etc/apache2/sites-available/default /etc/apache2/sites-available/example.com<br></br>sudo nano /etc/apache2/sites-available/example.com<br></br>ServerName example.com<br></br>ServerAlias www.example.com<br></br>DocumentRoot /var/www/example.com/public_html<br></br>sudo a2ensite example.com<br></br>sudo service apache2 restart<br></br>`