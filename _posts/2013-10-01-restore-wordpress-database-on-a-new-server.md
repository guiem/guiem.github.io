---
id: 771
title: 'Restore WordPress database on a new server'
date: '2013-10-01T22:21:08+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=771'
permalink: /restore-wordpress-database-on-a-new-server/
categories:
    - programming
    - wordpress
---

\[this post will be properly edited\]

I was creating the new database and WordPress would tell me to install the site.

Solution: dropped the database and created it from ‘mysql’ prompt.

user$ mysql -u root -p’yourpassword’ -h localhost  
mysql&gt; create database your\_database\_name;  
mysql&gt; exit  
user$ mysql -u root -p’yourpassword’ -h localhost your\_database\_name <db_to_import_from.sql></db_to_import_from.sql>