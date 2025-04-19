---
id: 574
title: 'WordPress in Spanish'
date: '2012-03-24T09:16:19+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=574'
permalink: /wordpress-in-spanish/
categories:
    - programming
    - wordpress
---

**Motivation**: it’s pretty simple. I just wanted to create a WordPress site in Spanish.  
**Solution**: download the file from the source specified below. Extract the file `es_ES.mo` and place it in `/wp-content/languages/`. Finally, change the file `wp-config.php` in the root directory to point to Spanish language: `define ('WPLANG', 'es_ES');`  
**Source**: [http://es.wordpress.org](http://es.wordpress.org/)