---
id: 769
title: 'Create a SSL Certificate on Ubuntu'
date: '2013-09-30T14:02:51+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=769'
permalink: /create-a-ssl-certificate-on-ubuntu/
categories:
    - programming
---

\[this post will be properly edited\]

sudo a2enmod ssl  
sudo service apache2 restart  
sudo mkdir /etc/apache2/ssl  
sudo nano /etc/apache2/sites-available/default

<virtualhost></virtualhost>

ServerName example.com:443

SSLEngine on  
SSLCertificateFile /etc/apache2/ssl/apache.crt  
SSLCertificateKeyFile /etc/apache2/ssl/apache.key

sudo a2ensite default  
sudo service apache2 reload

**source**: [digitalocean](https://www.digitalocean.com/community/articles/how-to-create-a-ssl-certificate-on-apache-for-ubuntu-12-04)