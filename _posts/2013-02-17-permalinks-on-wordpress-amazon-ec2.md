---
id: 653
title: 'Permalinks on WordPress (amazon EC2)'
date: '2013-02-17T10:57:52+00:00'
author: 'Guiem Bosch'
layout: single
guid: 'http://guiem.info/?p=653'
permalink: /permalinks-on-wordpress-amazon-ec2/
categories:
    - programming
    - wordpress
---

**Motivation**: in my particular case I moved a WordPress site from Bluehost to amazon’s EC2. Permalinks were not working.  
**Solution**: I had to modify the override option from my `httpd` service.

1. Go to `/etc/httpd/conf` and edit `httpd.conf````
    
    <directory></directory>
        Options FollowSymLinks
        AllowOverride All
    
    ```
2. Change also `AllowOverride` if it is set to `None`. ```
    
    # AllowOverride controls what directives may be placed in .htaccess files.
    # It can be "All", "None", or any combination of the keywords:
    #   Options FileInfo AuthConfig Limit
    #
        AllowOverride All
    ```
3. I you haven’t created it yet, place in the root directory of your wordpress installation a `.htaccess` file with the following contents: ```
    
    # BEGIN WordPress
    <ifmodule mod_rewrite.c="">
    RewriteEngine On
    RewriteBase /
    RewriteRule ^index\.php$ - [L]
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule . /index.php [L]
    </ifmodule>
    
    # END WordPress
    
    ```

**Source**: this [post](http://stackoverflow.com/questions/12292992/permalinks-on-wordpress-ec2 "stackoverflow").