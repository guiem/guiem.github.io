---
id: 753
title: 'How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu'
date: '2013-09-28T17:10:49+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=753'
permalink: /how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu/
categories:
    - programming
---

\[this post will be properly edited\]

`<br></br>sudo apt-get update<br></br>sudo apt-get install apache2<br></br>sudo apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql<br></br>sudo mysql_install_db<br></br>sudo /usr/bin/mysql_secure_installation # you can just say yes to all options<br></br>sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt<br></br>sudo nano /etc/apache2/mods-enabled/dir.conf # Add index.php to the beginning of index files<br></br>sudo service apache2 restart<br></br>`